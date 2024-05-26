from flask import Flask, request, render_template
from backend.app.models import db, ReportTemplate, VisualizationTemplate
from report_generator import generate_report
from visualization_module import visualize_report
from backend import create_db

app = Flask(__name__)
db.init_app(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Ошибка: файл не был предоставлен", 400
    file = request.files['file']
    file_path = file.filename
    new_report = ReportTemplate(name=file_path, content=file_path, json_file_path=file_path)
    db.session.add(new_report)
    db.session.commit()
    return "Файл успешно загружен"

@app.route('/add_visualization', methods=['POST'])
def add_visualization():
    if 'report_template_id' not in request.form or 'visualization_type' not in request.form:
        return "Ошибка: необходимые данные отсутствуют", 400
    report_template_id = int(request.form['report_template_id'])
    visualization_type = request.form['visualization_type']
    new_visualization = VisualizationTemplate(report_template_id=report_template_id, visualization_type=visualization_type, content="Пример содержимого")
    db.session.add(new_visualization)
    db.session.commit()
    return "Новая визуализация успешно добавлена"

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
