from flask import request
from flask import render_template
from flask.views import MethodView

class HomeController(MethodView):

    def __init__(self):
        pass

    def get(self):
        return render_template('app.html')
