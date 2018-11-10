from setuptools import setup

setup(
    name = 'mqtt-flask-app',
    version = '0.1',
    description = 'MQTT Flask app',
    url = 'https://github.com/joeladam518/mqtt-flask-app.git',
    author = 'Joel Haker',
    author_email = 'joeladam@gmail.com',
    license = 'MIT',
    packages = [
        'mqttflask',
    ],
    install_requires = [
        'flask',
        'flask_restful',
    ],
    zip_safe = False
)