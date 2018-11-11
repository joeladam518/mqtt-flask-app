from setuptools import setup

setup(
    name = 'mqttflask_app',
    version = '0.1',
    packages = [ 'site' ],
    install_requires = [
        'wheel',
        'uwsgi',
        'flask',
        'flask_restful',
        'python_dotenv',
        'click',
        'simplejson'
    ],
    license = 'MIT',
    description = 'A website',
)