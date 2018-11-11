import os
from dotenv import load_dotenv
from setuptools import setup

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

setup(
    name = 'mqttflask_app',
    version = os.getenv('VERSION'),
    packages = [ 'site' ],
    install_requires = [
        'wheel',
        'uwsgi',
        'flask',
        'flask_restful',
        'python_dotenv',
        'simplejson'
    ],
    license = 'MIT',
    description = 'A website for messing around with mqtt',
)
