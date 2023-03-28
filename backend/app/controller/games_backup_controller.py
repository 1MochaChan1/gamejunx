from app import flask_app, db, jsonify, request
import urllib3
from app.helpers import went_wrong, token_required, strike_through, get_platform
from app.models import  Game
from app.colored_print import DebugPrint, Colors
from app.controller import secret
import json

free_games_base_url = "https://free-to-play-games-database.p.rapidapi.com/api"
sale_games_base_url = "https://cheapshark-game-deals.p.rapidapi.com"

free_games_http = urllib3.PoolManager()
sale_games_http = urllib3.PoolManager()

free_games_http.headers = secret.free_games_http_headers
sale_games_http.headers = secret.sale_games_http_headers


@flask_app.route('/backup-games', methods=['POST'])
def backup_games():
    free_games: list[Game] = []
    sale_games: list[Game] = []
    res = {'status': 'success', 'message': 'none'}
    
    
    try:
        if (not (request.headers['Backup-Key'] == secret.backup_key)):
            return "Incorrect backup key in header."
        # flushing the db
        db.session.query(Game).delete()
        # Calling free games API
        free_games_res = free_games_http.request(
            'GET', free_games_base_url + "/games")
        free_games_decoded = free_games_res.data.decode('utf-8')
        free_games_json = json.loads(free_games_decoded)

        # `go` refers to `game object`.
        for go in free_games_json:
            _platform = get_platform(go['platform'])
            
            _game = Game(title=go['title'], description=go['short_description'],
                        tags=None, genre=go['genre'], platform=_platform,
                        price='free', img=go['thumbnail'],
                        link=go['freetogame_profile_url'])
            free_games.append(_game)
            db.session.add(_game)

        # Calling sales games API
        sale_games_res = sale_games_http.request(
            'GET', sale_games_base_url+"/deals")
        sale_games_decoded = sale_games_res.data.decode('utf-8')
        sale_games_json = json.loads(sale_games_decoded)

        for go in sale_games_json:
            # this flag checks if the current game should be skipped.
            should_skip=False

            # here i check if the current game on sale is already present in the `free_games` or `sale_games` list
            # if it is then we turn flag `should_skip` to True.
            for free_go in free_games:
                if(free_go.title == go['title']):
                    should_skip = True
                    break
            for sale_go in sale_games:
                if(sale_go.title == go['title']):
                    should_skip = True
                    break

            # if the flag is true the current game gets skipped.
            if(should_skip):
                continue

            _sale_price_float = float(go['salePrice'])
            sale_price = 'free' if _sale_price_float == 0.0 else f"$ {go['salePrice']}"
            base_price = f"$ {go['normalPrice']}"
            savings = f"$ {float(go['savings']):.2f}"

            description = f"You save {savings}, by paying {sale_price}   instead of {strike_through(base_price)}"

            # will remove this code block in future, it's here for testing
            _game = Game(title=go['title'], description=description,
                        tags=None, genre=None, platform=None,
                        price=sale_price, img=go['thumb'],
                        link=f"https://www.cheapshark.com/redirect?dealID={go['dealID']}")
            sale_games.append(_game)
            db.session.add(_game)

        # res['free_games'] = free_games
        # res['sale_games'] = sale_games

        db.session.commit()
        res ['message'] = f"{len(free_games)} Free Games and {len(sale_games)} Games on Sale backed up"
        return res

    except KeyError as ke:
        res['status']='error'
        res['message']='Backup key not found!'
        return res
    except Exception as e:
        return went_wrong(e)