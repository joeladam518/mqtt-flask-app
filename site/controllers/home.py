import os
from flask import request
from flask import render_template
from flask.views import MethodView

class HomeController(MethodView):

    def __init__(self):
        pass

    def get(self):
        data = {
            "css_version": os.getenv('CSS_VERSION'),
            "js_version": os.getenv('JS_VERSION')
        }
        return render_template('app.html', **data)
