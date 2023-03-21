from app import flask_app, db, request
from app.helpers import token_required, went_wrong, encode_password
from app.models import User
from app.colored_print import DebugPrint
import sqlalchemy


@flask_app.route('/user-details/basic', methods=['PUT', 'GET'])
@token_required
def change_name_details():
    res = {'status': 'success', 'message': 'User Successfully Updated!'}
    try:
        req = request.get_json()
        _user_raw: User = User.query.filter_by(id=req['id']).first()
        if (not _user_raw):
            res['status'] = "error"
            res['message'] = "User not found!"
            return res, 404
        match(request.method):
            case 'GET':
                res['message'] = "User found!"
                res['user'] = _user_raw.toMap()
                return res, 200

            case 'PUT':
                keys = req.keys()
                if ('name' in keys):
                    _user_raw.name = req['name']

                if ('username' in keys):
                    _user_raw.username = req['username']

                if ('email' in keys):
                    _user_raw.email = req['email']

                db.session.commit()
                _updated_user: User = User.query.filter_by(
                    id=req['id']).first()
                res['user'] = _updated_user.toMap()
                return res, 200

        return res, 200

    except sqlalchemy.exc.IntegrityError as i:
        properties = ['username', 'email']
        exception = str(i.orig)[1:-1].split(',')[1]
        property = list(x for x in properties if x in exception)[0].title()
        res['status'] = 'error'
        res['message'] = f"{property} already exists."
        return res, 409

    except Exception as e:
        return went_wrong(e)


@flask_app.route('/user-details/password', methods=['PUT'])
@token_required
def change_password():
    res = {'status': 'success', 'message': 'Password Successfully Updated!'}
    try:
        req = request.get_json()
        _user_raw: User = User.query.filter_by(id=req['id']).first()
        if (not _user_raw):
            res['status'] = "error"
            res['message'] = "User not found!"
            return res, 404
        
        if(encode_password(req['old_password']) == _user_raw.password):
            _user_raw.password = encode_password(req['new_password'])
            db.session.commit()
        else:
            res['status'] = "error"
            res['message'] = "Old password isn't valid!"
            return res, 400
        

        
        return res, 200

    except Exception as e:
        return went_wrong(e)
