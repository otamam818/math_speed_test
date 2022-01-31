import json
from os import path 

FILE: str = "../../data/records.json"
GAME_DESCRIPTION = {
    1 : "10 numbers",
    2 : "100 numbers",
    3 : "1000 numbers"
}

def import_json() -> dict: 
    if (not(path.exists(FILE))):
        create_json(FILE)
    return json.load(open(FILE))

def create_json(filename) -> None:
    EMPTY_JSON: str = '{}'
    with open(filename, 'w') as my_file:
        my_file.write(EMPTY_JSON)

def export_json(filename: str, json_data: dict) -> None: 
    with open(filename, 'w') as my_file:
        my_file.write(json.dumps(json_data))

def create_user(username: str) -> str: 
    """Creates a user if it does not exist. If a user exists, prompt again """
    INITIAL_SCORE: int = None
    json_dict: dict = import_json()
    while username in json_dict.keys():
        print("Username already exists. Please use another username")
    json_dict[username] = INITIAL_SCORE
    export_json(FILE, json_dict)
    return username

def get_score(username, game_choice) -> str:
    game_choice = GAME_DESCRIPTION[game_choice]
    return import_json()[username][game_choice]

def update_score(username, game_choice, score):
    """Updates the score of the user, based on their game choice"""
    current_game_description = GAME_DESCRIPTION[game_choice]
    json_dict = import_json()
    json_dict[username] = {current_game_description : round(score, 2)}
    export_json(FILE, json_dict)

