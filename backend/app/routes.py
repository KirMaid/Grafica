# import os
# from flask import Flask, flash, request, redirect, url_for
# from flask import render_template
# from app import app
# @app.route('/')
# def index():
#     user = {'username': 'Miguel'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#   form = LoginForm()
#   return render_template('upload.html', title='Upload file', form=form)
#
# def allowed_file(filename):
#     """ Функция проверки расширения файла """
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('Не удалось загрузить файл')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('Нет выбранного файла')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Загрузить новый файл</title>
#     <h1>Загрузить новый файл</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     </html>
#     '''


from app import app
@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"