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
    email = ""
    name = ""
    phone = ""
    cpf = ""
    address = ""
    game_time = ""
    timestamp = datetime.now()

actualUser = user()

@blueprint.route('/add_user', methods=[ 'POST' ])
def add_user():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    actualUser.name = str(form['name'])
    actualUser.email = str(form['email'])
    actualUser.phone = str(form['phone'])
    actualUser.cpf = str(form['cpf'])
    actualUser.address = str(form['address'])
    actualUser.game_time = "0"
    actualUser.timestamp = datetime.now()
    existingUser = bd.findUser(actualUser.cpf)
    if(existingUser != None):
        if(existingUser.game_time == "0"): print("Usuário " + str(existingUser.name) + " será o próximo a jogar")
        else: "Usuário já existe e já está com tempo cadastrado"
    else: 
        bd.InsertUser(actualUser)
        return "200"

    