from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired

class FileForm(FlaskForm):
  file = FileField('Выберите файл для постройки диаграммы')

