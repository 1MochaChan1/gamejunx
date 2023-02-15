from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.debug=True
flask_app.config.from_object(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/gamejunx_test'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(flask_app)


CORS(flask_app, resources={r"/*": {'origins': "*"}})
# CORS(app, resources={r"/*": {'origins': 'https://localhost:8080',
#      "allow-headers": "Access-Control-Allow-Origin"}})


# @flask_app.route('/', methods=['GET'])
# def greet():
#     return "Bitchi Noni"






# if __name__ == "__main__":
#     app.run(debug=True)

import app.views