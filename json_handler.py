import json
from os import path 

FILE: str = "records.json"

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

def update_json(function) -> None:
    json_dict: dict = import_json()
    # the function should return None, but in essence, mutate the dictionary
    function(json_dict)
    export_json(json_dict)

def create_user(username: str) -> str: 
    """Creates a user if it does not exist. If a user exists, prompt again """
    INITIAL_SCORE: int = 0
    json_dict: dict = import_json()
    while username in json_dict.keys():
        print("Username already exists. Please use another username")
    json_dict[username] = INITIAL_SCORE
    export_json(FILE, json_dict)
    return username

def get_score(username) -> str:
    return import_json()[username]

