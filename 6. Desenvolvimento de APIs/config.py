DEBUG = True

USERNAME = 'postgres'
PASSWORD = 'root'
SERVER = 'localhost'
PORT = '5432'
DB = 'db_cursoflask'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True