from flask import Flask, render_template, session, jsonify, request, make_response, session
import jwt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime, timedelta
from functools import wraps


flask_app = Flask(__name__)
flask_app.debug = True
flask_app.config.from_object(__name__)
flask_app.config['SECRET_KEY'] = 's7mbVzM_9FcL8gUd8Fc1'
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gamejunx_test'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(flask_app)


CORS(flask_app, resources={r"/*": {'origins': "*"}})

import app.router
import app.models