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
    game_time = "0"
    timestamp = datetime.now()

actualUser = user()

@blueprint.route('/next_player', methods=[ 'GET' ])
def next_player():
    global actualUser
    if(actualUser.cpf != "" and actualUser.game_time == "0"):
        context = {
            'email':actualUser.email,
            'name': actualUser.name,
            'phone':actualUser.phone,
            'cpf':actualUser.cpf,
            'address':actualUser.address,
            'game_time':actualUser.game_time,
            'timestamp':actualUser.timestamp,
        }
        actualUser = user()
        return context
    else:
        return "No player"

@blueprint.route('/update_user', methods=[ 'POST' ])
def update_user():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    print(str(res))
    bd.update_user(str(form['cpf']), (str(form['game_time'])))
    return "usuario atualizado"

@blueprint.route('/add_user', methods=[ 'POST' ])
def add_user():
    form = request.get_json(silent=True, force=True)
    res = (json.dumps(form, indent=3))
    existingUser = bd.find_user(str(form['cpf']))
    if(existingUser != None):
        if(existingUser.game_time == "0"): 
            actualUser.name = existingUser.name
            actualUser.email = existingUser.email
            actualUser.phone = existingUser.phone
            actualUser.cpf = existingUser.cpf
            actualUser.address = existingUser.address
            actualUser.game_time = existingUser.game_time
            return("Usuário " + str(existingUser.name) + " será o próximo a jogar")
        else: return("Usuário já existe e já está com tempo cadastrado")
    else: 
        actualUser.name = str(form['name'])
        actualUser.email = str(form['email'])
        actualUser.phone = str(form['phone'])
        actualUser.cpf = str(form['cpf'])
        actualUser.address = str(form['address'])
        actualUser.game_time = "0"
        actualUser.timestamp = datetime.now()
        bd.insert_user(actualUser)
        return "Usuário " + actualUser.name + " cadastrado com sucesso"

@blueprint.route('/users', methods=[ 'GET' ])
def show_users():
    context = {
        'users': bd.select_all_users()
    }
    return context

@blueprint.route('/reset_all', methods=[ 'GET' ])
def reset_timers():
    bd.reset_users()
    return "Cronômetros zerados!"

    