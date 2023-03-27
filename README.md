# gamejunx
Place for gamers to find Free Games and On-Sale Games, along with some insights(I haven't figured this part out, don't ask me.) on the games they own.


## Frontend Setup
### Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Lints and fixes files
```
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Backend Setup

### Install python modules
```
python -m pip install -r requirements.txt
```

### Create python environment
```
python -m venv ./backend/gamejunx_env
```

### Creating secrets
##### This has to be created by the dev. Create a file /app/controller/secret.py and follow the format below.
```
secret.py

free_games_http_headers = {                                                       
    "X-RapidAPI-Key": '[key for free games API]',                                 
    "X-RapidAPI-Host": "free-to-play-games-database.p.rapidapi.com"               
}                                                                                 
sale_games_http_headers = {                                                        
    "X-RapidAPI-Key": '[key for games on sale API]',                              
    "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"                      
}                                                                                  
                                                                                  
aws_database_password = '[passwd]'                                                
aws_database_uri = [AWS DB URL]                                                   
jwt_token_key = [JWT secret for creating token]                                   
```
