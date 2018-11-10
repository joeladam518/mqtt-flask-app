import os
from flask_restful import Resource

class HomeController():

    def index(self):
        return render_template('app.html')