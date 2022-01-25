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
        print("\nGood bye.")
        exit()

# Helper
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def start_game() -> None:
    """Input-based (and also the default) version of the game"""
    interface.greeting_message()
    user_name:  str = interface.select_user()
    user_score: str = json_handler.get_score(user_name)
    game_choice: int = interface.choose_options()
    while True:
        test_time(user_name, user_score, game_choice)

def test_time(username, user_score, game_choice):
    """Initiates the time-test for the user in the game"""
    option = { 1 : 10, 2 : 100, 3 : 1000 }[game_choice]
    initial_time = time()
    interface.test_math(username, user_score, option)
    final_time = time()
    interface.show_time(final_time-initial_time)

# Import convention
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
if __name__ == "__main__":
    main()

