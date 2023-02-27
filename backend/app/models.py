from app import db
from app.helpers import encode_password


# Will be used for email verification
class UnverifiedUser(db.Model):
    __tablename__ = "unverified_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    username = db.Column(db.String(400), unique=True, nullable=False)
    email = db.Column(db.String(400), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)

    def toMap(self):
        _map = {}
        _map['id'] = self.id
        _map['name'] = self.name
        _map['username'] = self.username
        _map['email'] = self.email
        return _map

    def __repr__(self):
        return f'User(id:{self.id},name:{self.name}, username:{self.username}, email:{self.email})'

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = encode_password(password)


# Users
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400),  nullable=False)
    username = db.Column(db.String(400), unique=True, nullable=False)
    email = db.Column(db.String(400), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    wishlist = db.relationship(
        'Wishlist', backref='user', lazy=True, cascade="all, delete")

    def toMap(self):
        _map: dict = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
        }
        return _map

    # factory method
    def fromJson(json: dict):
        _user = User(name=json['name'], username=json['username'],
                     email=json['email'], password=json['password'])
        return _user

    def __repr__(self):
        return f'User(id:{self.id},name:{self.name}, username:{self.username}, email:{self.email})'

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = encode_password(password)


"""
|- GAMES -----------------------------------------------------------|
|                                                                   |
|These game records are created only when the user adds them        |
|to his/her wishlist. If the title already exsists the operation    |
|gets skipped.                                                      |
|-------------------------------------------------------------------|
"""


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=True)
    tags = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    platform = db.Column(db.String(50), nullable=True)
    price = db.Column(db.String(20), nullable=False)
    img = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(200), nullable=True)

    def toMap(self) -> dict:
        _map: dict = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'tags': self.tags,
            'genre': self.genre,
            # converting the string to list here.
            'platform': self.platform,
            'price': self.price,
            'img': self.img,
            'link': self.link,
        }
        return _map

    # factory method
    def fromJson(self, json):
        _game = Game(title=json['title'], description=json['description'], tags=json['tags'],
                     genre=json['genre'], platform='_', price=json['price'], img=json['img'], link=json['link'])

        # converting platform list from API to string.
        if (isinstance(json['platform'], list)):
            _game.platform = ','.join(json['platform'])
        else:
            _game.platform = ''
        return _game

    def __repr__(self):
        return f'Game(id:{self.id},title:{self.title}, description:{self.description}, tags:{self.tags}, genre:{self.genre}, platform:{self.platform}, price:{self.price}, img:{self.img}, link:{self.link})'

    def __init__(self, title: str, description: str,
                 tags: str, genre: str,
                 platform: str, price: float,
                 img: str, link: str):
        self.title = title
        self.description = description
        self.tags = tags
        self.genre = genre
        self.platform = platform
        self.price = price
        self.img = img
        self.link = link


"""
|- WISHLIST -------------------------------------------------------|
|                                                                  |
|The wishlist is created at the time of creating a user account.   |
|                                                                  |
|Storing the game_ids as a String with a delimitter ','            |
|When converting to a map, turning the game_ids String into a list.|
|When fetching, it's being fetched as a String                     |
|------------------------------------------------------------------|
"""


class Wishlist(db.Model):
    __tablename__ = "wishlists"
    id = db.Column(db.Integer, primary_key=True)
    game_ids = db.Column(db.String(10000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def toMap(self) -> dict:
        _map: dict = {
            'id': self.id,
            'game_ids': self.game_ids.split(',')
        }
        return _map

    def fromJson(self, json):
        _wishlist = Wishlist(
            user_id=json['user_id']
        )

        # converting platform list from API to string.
        if (isinstance(json['platform'], list)):
            _wishlist.game_ids = ','.join(json['platform'])
        else:
            _wishlist.game_ids = ''
        return _wishlist

    def __repr__(self) -> str:
        return f'Wishlist(id:{self.id}, user_id:{self.user_id}, game_ids:{self.game_ids})'

    def __init__(self, game_ids: str, user_id: int):
        self.game_ids = game_ids
        self.user_id = user_id
