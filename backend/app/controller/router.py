from app import flask_app, session, request, jsonify, datetime, wraps,timedelta
from app.models import User
from app.helpers import encode_password, token_required
from app.colored_print import DebugPrint, Colors
import jwt

# <---- test ----> #
@flask_app.route('/test', methods=['GET'])
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
        _username_or_email = _json['username']
        _password = _json['password']
        _password_encrypted = encode_password(_password)

        _user_by_username = User.query.filter_by(
            username=_username_or_email, password=_password_encrypted).first()
        
        _user_by_email = User.query.filter_by(
            email=_username_or_email, password=_password_encrypted).first()
        
        if ((_user_by_username != None) or (_user_by_email != None)):
            _user:User =  _user_by_email if _user_by_email != None else _user_by_username
            session['logged_in'] = True

            token = jwt.encode({'user': _user.username, }, flask_app.config['SECRET_KEY'], algorithm='HS256')

            res['user'] = _user.toMap()
            res['token'] = token
            return jsonify(res)
        else:
            res['status'] = 'error'
            res['message'] = "We couldn't find the user"
            return jsonify(res), 403

    except Exception as e:
        DebugPrint(e, color=Colors.red)
        return jsonify({"error":"Something went wrong"}),500

