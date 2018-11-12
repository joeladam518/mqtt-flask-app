import os
from dotenv import load_dotenv

app_root = os.path.dirname(__file__)
dotenv_path = os.path.join(app_root, '.env')
load_dotenv(dotenv_path)

class Config(object):
    APPLICATION_ROOT = app_root
    SERVER_NAME = os.getenv('APP_URL')
    SECRET_KEY = os.getenv('APP_KEY')
    DEBUG = os.getenv('APP_DEBUG')
    MAX_CONTENT_LENGTH = os.getenv('MAX_CONTENT_LENGTH')
    PREFERRED_URL_SCHEME = os.getenv('PREFERRED_URL_SCHEME')
    TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD')
    EXPLAIN_TEMPLATE_LOADING = os.getenv('EXPLAIN_TEMPLATE_LOADING')
