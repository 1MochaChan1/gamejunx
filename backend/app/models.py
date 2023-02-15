from app import db
import hashlib

def encode_password(text:str)->str:
    encrypted_string:str= hashlib.md5(text.encode('utf')).hexdigest()
    return encrypted_string

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    username = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False)
    password = db.Column(db.String(400), nullable=False)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = encode_password(password)

