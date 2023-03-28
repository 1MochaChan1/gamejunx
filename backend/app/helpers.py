import hashlib
import traceback
from app.colored_print import Colors, DebugPrint
from app import request, wraps, jsonify, flask_app, db
from app.models import Wishlist, User
import jwt


def get_platform(platform:str):
    if('pc' in platform.lower()):
        return 'pc'
    elif('browser' in platform.lower()):
        return 'browser'
    else:
        return None

def strike_through(text):
    result = '\u0336'
    for c in text:
        result += c + '\u0336'
    return result

def encode_password(text:str)->str:
    encrypted_string:str= hashlib.md5(text.encode('utf')).hexdigest()
    return encrypted_string

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token=None
        if('Authorization' in request.headers.keys()):
            token=str(request.headers['Authorization'])[7:]
        if (not token):
            return jsonify({'error':'Token is missing!'}),401
        try:
            jwt.decode(token, flask_app.config['SECRET_KEY'],algorithms=['HS256'])
            return(func(*args, **kwargs))
        except Exception as e:
            went_wrong(e)
            return jsonify({"error":"Invalid Token"}), 498
    return decorated

def went_wrong(e:Exception):
    DebugPrint(e, color=Colors.red, end='\n------------------------\n')
    DebugPrint(''.join(traceback.TracebackException.from_exception(e).format()), color=Colors.error)
    return jsonify({"message":"Something went wrong", "status":"error"}),500

def create_wishlist(user:User) -> Wishlist:
    _wishlist: Wishlist = Wishlist(user_id=user.id)
    db.session.add(_wishlist)
    db.session.commit()
    return _wishlist
