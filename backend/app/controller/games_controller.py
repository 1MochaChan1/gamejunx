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
    try:
        json_raw = request.get_json()
        # fetch the client and their wishlist (if created)
        _user_raw: User = User.query.filter_by(id=json_raw['id']).first()
        _wishlist: Wishlist = Wishlist.query.filter_by(
            user_id=json_raw['id']).first()

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
                        res['games'].append(_game.toMap())
                res['message'] = f"Total {len(res['games'])} games in wishlist"
                return res

            # if game's is in wishlist -> add
            # else -> remove
            case 'PUT':
                _game: Game = Game.fromJson(json=json_raw['game'])
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
        return res

    except Exception as e:
        return went_wrong(e)


@flask_app.route('/get-games', methods=['GET'])
@token_required
def get_games():
    free_games: list[Game] = []
    sale_games: list[Game] = []
    res = {'status': 'success', 'message': 'none'}
    try:
        all_games: list[Game] = Game.query.all()
        raw_json = request.get_json()

        if (raw_json['id'] != None):
            _wishlist: Wishlist = Wishlist.query.filter_by(
                user_id=raw_json['id']).first()
            _wishlisted_games: list[str] = _wishlist.game_names.lower().split(
                ',') if (len(_wishlist.game_names) > 0) else []

        for game in all_games:
            _game_map = game.toMap()
            if (game.title.lower() in _wishlisted_games):
                _game_map['wishlisted'] = True
            else:
                _game_map['wishlisted'] = False
            if (game.price != "free"):
                sale_games.append(_game_map)
            else:
                free_games.append(_game_map)

        # Calling free games API
        # free_games_res = free_games_http.request(
        #     'GET', free_games_base_url + "/games")
        # free_games_decoded = free_games_res.data.decode('utf-8')
        # free_games_json = json.loads(free_games_decoded)

        # for go in free_games_json:
        #     _platform = get_platform(go['platform'])
        #     # will remove this code block in future, it's here for testing
        #     _game = Game(title=go['title'], description=go['short_description'],
        #                  tags=None, genre=go['genre'], platform=_platform,
        #                  price='free', img=go['thumbnail'],
        #                  link=go['freetogame_profile_url'])
        #     free_games.append(_game.toMap())

        # Calling sales games API
        # sale_games_res = sale_games_http.request(
        #     'GET', sale_games_base_url+"/deals")
        # sale_games_decoded = sale_games_res.data.decode('utf-8')
        # sale_games_json = json.loads(sale_games_decoded)

        # for go in sale_games_json:
        #     _sale_price_float = float(go['salePrice'])
        #     sale_price = 'free' if _sale_price_float == 0.0 else f"$ {go['salePrice']}"
        #     base_price = f"$ {go['normalPrice']}"
        #     savings = f"$ {float(go['savings']):.2f}"

        #     description = f"You save {savings}, by paying {sale_price}   instead of {strike_through(base_price)}"

        #     # will remove this code block in future, it's here for testing
        #     _game = Game(title=go['title'], description=description,
        #                  tags=None, genre=None, platform=None,
        #                  price=sale_price, img=go['thumb'],
        #                  link=f"https://www.cheapshark.com/redirect?dealID={go['dealID']}")
        #     sale_games.append(_game.toMap())

        res['free_games'] = free_games
        res['sale_games'] = sale_games
        return jsonify(res)
    except Exception as e:
        return went_wrong(e)
