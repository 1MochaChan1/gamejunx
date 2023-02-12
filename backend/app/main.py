from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})
# CORS(app, resources={r"/*": {'origins': 'https://localhost:8080',
#      "allow-headers": "Access-Control-Allow-Origin"}})

# hello world route
@app.route('/', methods=['GET'])
def greet():
    return "Kya hai be lavde"

if __name__ == "__main__":
    app.run(debug=True)