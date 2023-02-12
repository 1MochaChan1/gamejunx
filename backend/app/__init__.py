from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import hashlib

flask_app = Flask(__name__)
flask_app.debug=True
flask_app.config.from_object(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gamejunx_test'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(flask_app)

CORS(flask_app, resources={r"/*": {'origins': "*"}})
# CORS(app, resources={r"/*": {'origins': 'https://localhost:8080',
#      "allow-headers": "Access-Control-Allow-Origin"}})

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

@flask_app.route('/', methods=['GET'])
def greet():
    return "Bitchi Noni"

@flask_app.route('/users', methods=['GET'])
def users():
    all_data = User.query.all()
    user:User = all_data[0]
    return user.username




# if __name__ == "__main__":
#     app.run(debug=True)
