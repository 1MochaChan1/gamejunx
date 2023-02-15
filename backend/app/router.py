from app import flask_app, session
from app.models import User

# landing
@flask_app.route('/', methods=['GET'])
def landing():
    if(session.get('logged_in')):
        return "User Logged in"
    else:
        return "User not logged in, please signin."
    
# login
@flask_app.route('/login', methods=['POST'])
def login():
    # _username = request.form['username'];
    # all_data = User.query.filter_by(username=_username);
    # if(len(all_data)):
    return {};



# users
@flask_app.route('/users', methods=['GET'])
def users():
    all_data = User.query.all()
    user:User = all_data[0]
    return user.username

