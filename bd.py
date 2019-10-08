
from flask_sqlalchemy import SQLAlchemy
 	
from datetime import datetime


db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    cpf = db.Column(db.String(11))
    address = db.Column(db.String(140))
    game_time = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime())
    def __init__(self, email, name, phone, cpf, address, game_time, timestamp):
        self.email = email
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.address = address
        self.game_time = game_time
        self.timestamp = timestamp

def insert_user(data):
    usr = users(data.email, data.name, data.phone, data.cpf, data.address, data.game_time, data.timestamp)
    db.session.add(usr)
    db.session.commit()

def select_all_users():
    data_users = users.query.all()
    usersData = []
    for num, item in enumerate(data_users, start=0):
        context = {
            'id': item.id,
            'email':str(item.email),
            'name':str(item.name),
            'phone':str(item.phone),
            'cpf':str(item.cpf),
            'address':str(item.address),
            'game_time':str(item.game_time),
            'timestamp':str(item.timestamp),
        }
        usersData.insert(num, context)
    return(usersData)

def find_user(userCpf):
    user = users.query.filter_by(cpf=userCpf).first()
    if(user != None): return user
    else: return None

def update_user(userCpf, new_game_time):
    upd = db.update(users).where(users.cpf == userCpf).values(game_time=new_game_time)
    db.session.execute(upd)
    db.session.commit()