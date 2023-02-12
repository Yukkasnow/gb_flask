import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = 'SECRET_KEY'

SQLALCHEMY_DATABASE_URI ="sqlite:///db.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True