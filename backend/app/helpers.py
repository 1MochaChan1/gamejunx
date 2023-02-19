import hashlib
from app.colored_print import Colors, DebugPrint
from app import request, wraps, jsonify, flask_app
import jwt

def encode_password(text:str)->str:
    encrypted_string:str= hashlib.md5(text.encode('utf')).hexdigest()
    return encrypted_string

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token=None
        DebugPrint(request.headers)
        if('Authorization' in request.headers.keys()):
            token=str(request.headers['Authorization'])[7:]
        if (not token):
            return jsonify({'Alert':'Token is missing!'}),401
        try:
            jwt.decode(token, flask_app.config['SECRET_KEY'],algorithms=['HS256'])
            return(func(*args, **kwargs))
        except Exception as e:
            DebugPrint(e)
            return jsonify({"error":"Invalid Token"}), 498
    return decorated

def went_wrong(e:Exception):
    DebugPrint(e, color=Colors.red)
    return jsonify({"error":"Something went wrong"}),500