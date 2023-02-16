from app import flask_app, session, request, jsonify, datetime, wraps,timedelta
from app.models import User
from app.helpers import encode_password
from app.colored_print import DebugPrint, Colors
import jwt

# functions will only work if the token is verified
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

# <---- landing ----> #
@flask_app.route('/', methods=['GET'])
@token_required
def landing():
    return "User Logged in"

# testing
@flask_app.route('/testing', methods=['GET'])
@token_required
def token_page():
    return jsonify({"content":"JWT verified, welcome to dashboard"})


# <---- login ----> #
@flask_app.route('/login', methods=['POST'])
def login():
    #TODO: use this with make_response()
    res = {'status': 'success', 'message': 'none'}
    try:
        _json = request.get_json()
        _username = _json['username']
        _password = _json['password']
        _password_encrypted = encode_password(_password)

        _user = User.query.filter_by(
            username=_username, password=_password_encrypted).first()

        if (_user):
            session['logged_in'] = True

            token = jwt.encode({'user': _username, 'expiration': str(
                datetime.utcnow()+timedelta(seconds=600))}, flask_app.config['SECRET_KEY'], algorithm='HS256')

            res['user'] = _user.toMap()
            res['token'] = token
            return jsonify(res)
        else:
            res['status'] = 'error'
            res['message'] = "We couldn't find the user"
            return jsonify(res), 403

    except:
        return jsonify({"error":"Something went wrong"}),500


# <---- users ----> #
@flask_app.route('/users', methods=['GET'])
def users():
    all_data = User.query.all()
    user: User = all_data[0]
    return user.username
