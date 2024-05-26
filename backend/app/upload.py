import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in in app.config['ALLOWED_EXTENSIONS']

class FileForm(FlaskForm):
    file = FileField('Выберите файл для постройки диаграммы', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = FileForm()
    if form.validate_on_submit():
        file = form.file.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'Файл {filename} успешно загружен.')
            return redirect(url_for('download_file', name=filename))
    return render_template('upload.html', form=form)

@app.route('/download/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

if __name__ == '__main__':
    app.run(debug=True)
