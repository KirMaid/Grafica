from flask import Flask, request, render_template
from models import db, ReportTemplate, VisualizationTemplate
from report_generator import generate_report
from visualization_module import visualize_report

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reports.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = file.filename  # Сохраняем имя файла как путь к файлу
    # Здесь должна быть логика сохранения пути к файлу в базе данных
    new_report = ReportTemplate(name=file_path, content=file_path, json_file_path=file_path)
    db.session.add(new_report)
    db.session.commit()
    return "Файл успешно загружен"

@app.route('/generate_report', methods=['POST'])
def generate():
    file_path = request.form['file_path']
    template_id = request.form['template_id']
    report_content = generate_report(file_path, template_id)
    return report_content

@app.route('/visualize_report', methods=['POST'])
def visualize():
    report_content = request.form['report_content']
    visualization_template_id = request.form['visualization_template_id']
    visualization_content = visualize_report(report_content, visualization_template_id)
    return visualization_content

if __name__ == '__main__':
    app.run(debug=True)
