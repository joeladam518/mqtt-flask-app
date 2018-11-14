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
        'flask_httpauth',
        'python_dotenv',
        'simplejson',
        'paho-mqtt',
    ],
    license = 'MIT',
    description = 'A website for messing around with mqtt',
)
