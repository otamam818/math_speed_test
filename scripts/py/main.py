# Imports
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
import json_handler
import interface

from time import time, localtime

# Main
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def main() -> None:
    """Program for switching between different TUI and GUI"""
    try:
        start_game()
    except KeyboardInterrupt:
        interface.leave_program()

# Helper
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def start_game() -> None:
    """Input-based (and also the default) version of the game"""
    scores = []
    interface.greeting_message()

    user_name:  str = interface.select_user()
    game_choice: int = interface.choose_options(user_name)
    try:
        test_time(user_name, game_choice, scores)
    except KeyboardInterrupt:
        interface.request_overwrite_score(user_name, scores, game_choice)

def test_time(username, game_choice, scores: list):
    """Initiates the time-test for the user in the game"""
    while True:
        option = { 1 : 10, 2 : 100, 3 : 1000 }[game_choice]
        initial_time = time()
        interface.test_math(username, option)
        final_time = time()
        temp_score = final_time-initial_time
        interface.show_time(temp_score)
        scores.append(temp_score)

# Import convention
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
if __name__ == "__main__":
    main()

