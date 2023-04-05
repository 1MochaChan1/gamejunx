import gevent.monkey
gevent.monkey.patch_all()
from app import application, session, request, jsonify, make_response, db
from app.models import User
from app.helpers import encode_password, went_wrong, create_wishlist
from app.colored_print import DebugPrint, Colors
import jwt


 

# <---- test ----> #
@application.route('/test', methods=['GET'])
# @token_required
def token_page():
    return "<h1> Hello </h1>"


# <---- login ----> #
@application.route('/login', methods=['POST'])
def login():
    #TODO: use this with make_response()
    res = {'status': 'success', 'message': 'Login Successful!'}
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

            token = jwt.encode({'user': _user.username, }, application.config['SECRET_KEY'], algorithm='HS256')

            res['user'] = _user.toMap()
            res['token'] = token
            return jsonify(res)
        else:
            res['status'] = 'error'
            res['message'] = "We couldn't find the user"
            return jsonify(res), 403

    except Exception as e:
        return went_wrong(e)


# <---- signup ----> #
@application.route('/signup', methods=['POST'])
def signup():
    res = {'status': 'success', 'message': 'User Successfully Created!'}
    _response = make_response(res)
    try:
        _json = request.get_json()
        _user: User = User.fromJson(json=_json)

        matching_username = User.query.filter_by(
            username=_user.username).first()
        matching_email = User.query.filter_by(email=_user.email).first()

        if ((matching_username == None) and (matching_email == None)):
            # First create user
            res['message'] = 'success'
            res['status'] = 'none'
            db.session.add(_user)
            db.session.commit()

            # Based on user, create a wishlist    
            create_wishlist(_user)
            # _wishlist = Wishlist(user_id=_user.id);
            # db.session.add(_wishlist)
            # db.session.commit()
            return _response

        if (matching_username):
            res['message'] = 'Username already exists'
            res['status'] = 'error'
            _response = make_response(res)
            _response.status_code = 400
            _response.mimetype = 'application/json'
            return _response

        if (matching_email):
            res['message'] = 'Email already exists'
            res['status'] = 'error'
            _response = make_response(res)
            _response.status_code = 400
            _response.mimetype = 'application/json'
            return _response

        return _response
    except Exception as e:
        return went_wrong(e)


# <---- email - verificaiton ----> #
@application.route('/verify-email')
def verify_email():

    res = {'status': 'success', 'message': 'Email Available'}
    response = make_response(res)
    try:
        _json = request.get_json()
        _email = _json['email']
        _matching_email = User.query.filter_by(
            email=_email).first()

        if _matching_email:
            res['message'] = 'Email already exists'
            res['status'] = 'error'
            response = make_response(res)
            response.status_code = 400
            response.mimetype = 'application/json'
        else:
            response = make_response(res)
            response.status_code = 200
            response.mimetype = 'application/json'

        return response

    except Exception as e:
        return went_wrong(e)


# <---- username - verfication ----> #
@application.route('/verify-username')
def verify_username():
    res = {'status': 'success', 'message': 'Username Available'}
    response = make_response(res)
    try:
        _json = request.get_json()
        _username = _json['username']
        matching_username = User.query.filter_by(
            username=_username).first()

        if matching_username:
            res['message'] = 'Username already exists'
            res['status'] = 'error'
            response = make_response(res)
            response.status_code = 400
            response.mimetype = 'application/json'
        else:
            response = make_response(res)
            response.status_code = 200
            response.mimetype = 'application/json'

        return response
    except Exception as e:
        return went_wrong(e)

