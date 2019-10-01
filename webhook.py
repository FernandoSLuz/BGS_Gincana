import sys
import os
import time
import json

import flask
from flask import request
import requests as req
from flask import Blueprint
import bd

blueprint = flask.Blueprint('webhook', __name__)

@blueprint.route('/webhook', methods=[ 'POST', 'GET' ])
def webhook():
    #form = request.get_json(silent=True, force=True)
    #res = (json.dumps(form, indent=3))
    #print(res)
    #recievedPhoneStr = str(form['data']['fromNumber'])
    #recievedMessage = str(form['data']['body'])
    phones = bd.SelectAllUsers()
    context = {
        'title': phones
    }
    return context