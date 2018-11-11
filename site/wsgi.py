from mqttflask import app
from werkzeug.debug import DebuggedApplication

if __name__ == '__main__':
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

    app.run()
