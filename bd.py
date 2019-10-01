
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    timestamp = db.Column(db.DateTime(100))
    def __init__(self, name, email, phone, timestamp):
        self.name = phone
        self.email = name
        self.phone = phone
        self.timestamp = timestamp

def SelectAllUsers():
    data_users = users.query.all()
    usersList = ""
    for num, item in enumerate(data_users, start=0):
        usersList += "Name: " + str(item.name) + " --- phone " + str(item.phone) + " --- date " + str(item.timestamp) + " ----"
    return(usersList)