import os
from dotenv import load_dotenv
from setuptools import setup

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

setup(
    name = 'mqttflask_app site package',
    version = os.getenv('VERSION'),
    packages = [ 'controllers' ],
    description = 'This package holds the actual website.',
)