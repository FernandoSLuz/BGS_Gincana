import sys
import os
import time
import json
from datetime import datetime

import flask
from flask import request
import requests as req
from flask import Blueprint
import bd

blueprint = flask.Blueprint('webhook', __name__)

class user():
    name = ""
    email = ""
    phone = ""

actualUser = user()

@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def newUser():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    actualUser.name = str(form['name'])
    actualUser.email = str(form['email'])
    actualUser.phone = str(form['phone'])
    try:
        bd.InsertUser(actualUser)
    except:
        return "Usuário já existente"
    return "true"