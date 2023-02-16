# launching python venv
source D:/4_Projects/4_Backend/gamejunx/backend/gamejunx_env/Scripts/activate

# setting flask to debug
cd app
export FLASK_APP=app
export FLASK_DEBUG=1

# running flask app
cd ..
flask --app app run
