from app import flask_app, db, jsonify
import urllib3
from app.helpers import went_wrong, token_required, strike_through, get_platform
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

@flask_app.route('/get-games', methods=['GET'])
@token_required
def get_games():
    free_games: list[Game] = []
    sale_games: list[Game] = []
    res = {'status': 'success', 'message': 'none'}
    try:
        # Calling free games API
        free_games_res = free_games_http.request(
            'GET', free_games_base_url + "/games")
        free_games_decoded = free_games_res.data.decode('utf-8')
        free_games_json = json.loads(free_games_decoded)

        for go in free_games_json:
            _platform = get_platform(go['platform'])
            # will remove this code block in future, it's here for testing
            _game = Game(title=go['title'], description=go['short_description'],
                         tags=None, genre=go['genre'], platform=_platform,
                         price='free', img=go['thumbnail'],
                         link=go['freetogame_profile_url'])
            free_games.append(_game.toMap())

        # Calling sales games API
        sale_games_res = sale_games_http.request(
            'GET', sale_games_base_url+"/deals")
        sale_games_decoded = sale_games_res.data.decode('utf-8')
        sale_games_json = json.loads(sale_games_decoded)

        for go in sale_games_json:
            sale_price = 'free' if go['salePrice'][0] == "0" else f"$ {go['salePrice']}"
            base_price = f"$ {go['normalPrice']}"
            savings = f"$ {float(go['savings']):.2f}"

            description = f"You save {savings}, by paying {sale_price}   instead of {strike_through(base_price)}"

            # will remove this code block in future, it's here for testing
            _game = Game(title=go['title'], description=description,
                         tags=None, genre=None, platform=None,
                         price=sale_price, img=go['thumb'],
                         link=f"https://www.cheapshark.com/redirect?dealID={go['dealID']}")
            sale_games.append(_game.toMap())
            
        res['free_games'] = free_games
        res['sale_games'] = sale_games
        return jsonify(res)
    except Exception as e:
        return went_wrong(e)
