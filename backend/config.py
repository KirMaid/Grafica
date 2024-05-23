import os
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or '/uploads'
  ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS') or {'csv'}
  MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 16 * 1000 * 1000
  SQLALCHEMY_DATABASE_URI = 'mysql://root:mysecretpassword@db-service/example'
