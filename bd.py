
from flask_sqlalchemy import SQLAlchemy
 	
from datetime import datetime


db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    timestamp = db.Column(db.DateTime(100))
    gametime = db.Column(db.String(100))
    def __init__(self, name, email, phone, timestamp, gametime):
        self.name = name
        self.email = email
        self.phone = phone
        self.timestamp = timestamp
        self.gametime = gametime

def InsertUser(data):
    usr = users(data.name, data.email, data.phone, datetime.now(), "0")
    db.session.add(usr)
    db.session.commit()

def SelectAllUsers():
    data_users = users.query.all()
    usersList = ""
    for num, item in enumerate(data_users, start=0):
        usersList += "Name: " + str(item.name) + " --- phone " + str(item.phone) + " --- date " + str(item.timestamp) + " ----"
    return(usersList)