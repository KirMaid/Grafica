import pandas as pd
from backend.app.models import ReportTemplate


def generate_report(file_path, template_id):
    """
    Генерирует отчет на основе загруженного файла и выбранного шаблона отчета.

    :param file_path: Путь к файлу с данными.
    :param template_id: ID выбранного шаблона отчета.
    :return: Содержимое сформированного отчета.
    """
    # Загрузка файла и преобразование в DataFrame
    df = pd.read_csv(file_path)

    # Получение шаблона отчета
    template = ReportTemplate.query.get(template_id)

    # Примерная логика формирования отчета
    # Здесь может быть использована любая логика обработки данных, например, фильтрация, агрегация, сортировка и т.д.
    # Предположим, что шаблон отчета указывает на необходимость агрегации данных по определенным полям
    aggregated_data = df.groupby('column_to_aggregate').sum()  # Пример агрегации

    # Преобразование агрегированных данных в строку отчета
    report_content = aggregated_data.to_string()

    return report_content
