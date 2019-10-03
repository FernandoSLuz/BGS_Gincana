import sys
import os
import time

import flask
import requests

from webhook import blueprint as webhook_blueprint
import bd

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(webhook_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ubergeek@localhost/bgs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bd.db = bd.SQLAlchemy(app)

@app.route('/')
def index():
    context = {
        'title':'Hacka | Pepe'
    }
    return (context)

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)
    app.run(host='0.0.0.0')