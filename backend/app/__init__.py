from flask import Flask, render_template, session, jsonify, request, make_response, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy, query

from datetime import datetime, timedelta
from functools import wraps

from app.controller import secret

application = Flask(__name__)
application.debug = True
application.config.from_object(__name__)
application.config['SECRET_KEY'] = secret.jwt_token_key
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gamejunx_test'
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = secret.aws_database_uri
application.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(application)


CORS(application, resources={r"/*": {'origins': "*"}})

import app.controller.auth_controller
import app.controller.signup_controller
import app.controller.games_controller
import app.controller.user_details_controller
import app.controller.games_backup_controller

import app.models
import app.helpers

