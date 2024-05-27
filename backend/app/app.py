from flask import Flask, request, render_template
from backend.app import models
from report_generator import generate_report
from visualization_module import visualize_report
# from backend.app import create_db
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import io
import base64

app = Flask(__name__)
# db.init_app(app)

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


def show():
    df = pd.read_csv('data.csv')
    fig = px.line(df, x='date', y='value', title='Данные из CSV-файла')
    graph_bytes = io.BytesIO()
    fig.write_image(graph_bytes, format='png')
    graph_bytes.seek(0)
    graph_url = base64.b64encode(graph_bytes.getvalue()).decode()

    return render_template('grafic.html', graph_url=graph_url)


if __name__ == '__main__':
    # create_db()
    app.run(debug=True)
