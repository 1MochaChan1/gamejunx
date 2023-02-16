from app import db
from app.helpers import encode_password


class UnverifiedUser(db.Model):
    __tablename__="unverified_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    username = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False)
    password = db.Column(db.String(400), nullable=False)

    def toMap(self):
        _map = {}
        _map['id']=self.id
        _map['name']=self.name
        _map['username']=self.username
        _map['email']=self.email
        return _map

    def __repr__(self):
        return f'User(id:{self.id},name:{self.name}, username:{self.username}, email:{self.email})'

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = encode_password(password)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    username = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False)
    password = db.Column(db.String(400), nullable=False)

    def toMap(self):
        _map = {}
        _map['id']=self.id
        _map['name']=self.name
        _map['username']=self.username
        _map['email']=self.email
        return _map

    def __repr__(self):
        return f'User(id:{self.id},name:{self.name}, username:{self.username}, email:{self.email})'

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = encode_password(password)
