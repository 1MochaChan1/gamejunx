from app import flask_app, session, request, jsonify, db, make_response, query
from app.colored_print import Colors, DebugPrint
from app.helpers import went_wrong
from app.models import User, Wishlist


# <---- signup ----> #
@flask_app.route('/signup', methods=['POST'])
def signup():
    res = {'status': 'success', 'message': 'none'}
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

            # Based on user create a wishlist    
            _wishlist = Wishlist(game_ids=None, user_id=_user.id);
            db.session.add(_wishlist)
            db.session.commit()
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
        went_wrong(e)


# <---- email - verificaiton ----> #
@flask_app.route('/verify-email')
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
        went_wrong(e)


# <---- username - verfication ----> #
@flask_app.route('/verify-username')
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
        went_wrong(e)
