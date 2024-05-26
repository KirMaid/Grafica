import matplotlib.pyplot as plt
from backend.app.models import VisualizationTemplate


def visualize_report(report_content, visualization_template_id):
    """
    Визуализирует отчет по заданному шаблону визуализации.

    :param report_content: Содержимое сформированного отчета.
    :param visualization_template_id: ID выбранного шаблона визуализации.
    :return: Визуализированный отчет в виде изображения.
    """
    # Получение шаблона визуализации
    visualization_template = VisualizationTemplate.query.get(visualization_template_id)

    # Примерная логика визуализации
    # Здесь может быть использована любая логика визуализации, в зависимости от типа данных и требований к визуализации
    # Предположим, что шаблон визуализации указывает на необходимость построения графика линий
    data = report_content.split('\n')  # Пример разделения содержимого отчета на строки
    x_values = [i for i, _ in enumerate(data)]  # Индексы строк
    y_values = [float(value) for value in data if value.isdigit()]  # Значения из строк

    # Построение графика линий
    plt.plot(x_values, y_values)
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.title('Visualization of Report Data')

    # Сохранение графика в файл
    plt.savefig('report_visualization.png')

    return 'report_visualization.png'  # Возвращаем путь к файлу с визуализацией
