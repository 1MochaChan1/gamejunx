from app import flask_app,  jsonify, request, db
import urllib3
from app.helpers import went_wrong, token_required, create_wishlist
from app.models import User, Wishlist, Game
from app.colored_print import DebugPrint, Colors
from app.controller import secret
import json

free_games_base_url = "https://free-to-play-games-database.p.rapidapi.com/api"
sale_games_base_url = "https://cheapshark-game-deals.p.rapidapi.com"

free_games_http = urllib3.PoolManager()
sale_games_http = urllib3.PoolManager()

free_games_http.headers = secret.free_games_http_headers
sale_games_http.headers = secret.sale_games_http_headers


@flask_app.route('/wishlist', methods=['GET', 'PUT'])
@token_required
def add_remove_wishlist():
    res = {'status': 'success', 'message': 'none'}
    u_id = None
    _game_for_wishlist = {}
    try:
        is_json = False
        if ('Content-Type' in request.headers):
            is_json = request.headers['Content-Type'] == 'application/json'
            if (is_json):
                u_id = request.get_json()['user_id']
                _game_for_wishlist = request.get_json()['game']
        elif('user_id' in request.args):
            u_id = request.args['user_id']
        else:
            raise KeyError("user_id")


        # fetch the client and their wishlist (if created)
        _user_raw: User = User.query.filter_by(id=u_id).first()
        _wishlist: Wishlist = Wishlist.query.filter_by(
            user_id=u_id).first()

        # create a wishlist if not created.
        if (_wishlist == None):
            _wishlist = create_wishlist(_user_raw)

        # converting string to list and storing it to `_wishlist_games` to make validation easier.
        _wishlisted_games: list[str] = _wishlist.game_names.lower().split(
            ',') if (len(_wishlist.game_names) > 0) else []

        match(request.method):
            # return all the games that are available in the wishlist
            case 'GET':
                res['games'] = []
                _all_games: list[Game] = Game.query.all()
                for _game in _all_games:
                    if (_game.title.lower() in _wishlisted_games):
                        _game_map = _game.toMap()
                        _game_map['wishlisted'] = True
                        res['games'].append(_game_map)
                res['message'] = f"Total {len(res['games'])} games in wishlist"
                return res

            # if game's is in wishlist -> add
            # else -> remove
            case 'PUT':
                _game: Game = Game.fromJson(json=_game_for_wishlist)
                if (not _user_raw):
                    res['status'] = "error"
                    res['message'] = "User not found!"
                    return res, 404
                else:
                    if (_game.title.lower() in _wishlisted_games):
                        _wishlisted_games.remove(_game.title.lower())
                        res['message'] = f"{_game.title} successfully removed from Wishlist"
                    else:
                        _wishlisted_games.append(_game.title.lower())
                        res['message'] = f"{_game.title} successfully added to Wishlist"

                    _wishlist.game_names = ','.join(_wishlisted_games)
                    db.session.add(_wishlist)
                    db.session.commit()
                    return res

    except KeyError as ke:
        res['status'] = "error"
        res['message'] = f"Field {str(ke)} is missing!"
        DebugPrint(ke)
        return res, 400

    except Exception as e:
        return went_wrong(e)


@flask_app.route('/get-games', methods=['GET'])
@token_required
def get_games():
    free_games: list[Game] = []
    sale_games: list[Game] = []
    res = {'status': 'success', 'message': 'none'}
    id = None
    try:
        all_games: list[Game] = Game.query.all()
        is_json = False
        if ('Content-Type' in request.headers):
            is_json = request.headers['Content-Type'] == 'application/json'
            if (is_json):
                id = request.get_json()['user_id']
        elif ('user_id' in request.args):
            id = request.args['user_id']

        if (id):
            _wishlist: Wishlist = Wishlist.query.filter_by(
                user_id=id).first()
            _wishlisted_games: list[str] = _wishlist.game_names.lower().split(
                ',') if (len(_wishlist.game_names) > 0) else []

        for game in all_games:
            _game_map = game.toMap()

            if (id):
                if (game.title.lower() in _wishlisted_games):
                    _game_map['wishlisted'] = True
                else:
                    _game_map['wishlisted'] = False

            if (game.price != "free"):
                sale_games.append(_game_map)
            else:
                free_games.append(_game_map)

        res['free_games'] = free_games
        res['sale_games'] = sale_games
        return jsonify(res)

    except Exception as e:
        return went_wrong(e)
