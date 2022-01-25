# Imports
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
import json_handler
import subprocess

import random
import colors

from typing import Final, List, Union

# Constants
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
NUMBER_CHOICE: str = "\nPick a number: "
YES_NO_CHOICE: str = "\n1. Yes\n2. No" + NUMBER_CHOICE
SEPARATOR = '―'*20
SYMBOLS = "+-*/"

# Special datatypes
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
Number = Union[int, float]
# ENUM
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
SUCCESS = object()
FAILURE = object()

# Functions
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def greeting_message() -> None:
    separate()
    print("Welcome to the math tester,", 
        "where we test your speed in basic maths.")
    show_exit_shortcut()

def separate(color = colors.BLUE) -> None:
    colors.echo(SEPARATOR, color)

def select_user() -> str:
    """
    Asks the user to select a username if available. If not, creates a new
    user in the records json file.
    Returns the username.
    """
    records: dict = json_handler.import_json()
    records_not_empty: bool = len(records) > 0
    user_list: list = list(records)

    separate()
    if records_not_empty:
        print("Current users: ")
        count = 1
        for user in user_list:
            print(f"{count}. {user}")
            count += 1
        separate()
        print("0. Create user")
        options = [str(i) for i in range(0, count)]
        number_choice = validate_int_choice(options)
        # The number can be uesd to choose a user from the records dict
        if number_choice == 0:
            user_choice = make_new_user()
        else:
            user_choice = user_list[number_choice-1]
    else:
        choice = input("No user available. Create new? " + YES_NO_CHOICE)
        YES = '1'
        NO  = '2'
        if choice == YES:
            user_choice = make_new_user()
        elif choice == NO:
            leave_program(SUCCESS)
    return user_choice

def show_exit_shortcut() -> None:
    print("Press CTRL+C to quit")

def choose_options() -> int:
    options: str = "\n".join([
        "1. Test for 10 numbers",
        "2. Test for 100 numbers",
        "3. Test for 1000 numbers"
    ])
    separate()
    print("We have 3 options:\n" + options)
    options: List[str] = list("123")
    choice: int = validate_int_choice(options)
    return choice

def validate_int_choice(options: List[str]) -> int:
    choice = input("Choose an option: ")

    while choice not in options:
        print("Invalid option.")
        choice = input("Please pick a number from those provided: ")
    return int(choice)

def make_new_user() -> str:
    username = input("Enter username: ")
    return json_handler.create_user(username)

def test_math(username, score, option):
    """Tests the user with mathematic questions"""
    # A symbol needs to be unbiasedly chosen to test against
    chosen_symbol = random.choice(SYMBOLS)
    symbol_arg = {
        '+' : "-a",
        '-' : "-s",
        '*' : "-m",
        '/' : "-d"
    }[chosen_symbol]

    # Invoked from the commandline for eventually scaling the app
    command = f"python3 cli.py -g {option} {symbol_arg}"
    question = subprocess.getoutput(command)

    # Calculated values need to be presented to the user
    separate(color=colors.YELLOW)
    given_answer: Number = get_numerical_response(question)

    # Check whether the user gave the correct answer
    actual_answer: Number = parse_answer(question, chosen_symbol)

    assess_answer(given_answer, actual_answer)

def assess_answer(given_answer: Number, actual_answer: Number) -> None:
    answer_matches: bool = compare_answers(given_answer, actual_answer)
    if answer_matches:
        colors.echo("Correct answer! ", colors.GREEN, end='')
        print("Good Job!")
    else:
        colors.echo("Incorrect answer!", colors.RED)
        print("The correct answer is ", end='')
        colors.echo(actual_answer, colors.YELLOW)

def get_numerical_response(question: str) -> Number:
    answer: str = input(question + " = ").strip()
    MINUS_SIGN: str = '-'

    is_negative: bool
    if MINUS_SIGN in answer:
        is_negative = True
        answer = answer.replace(MINUS_SIGN, '')
    else:
        is_negative = False

    is_number: bool = is_float(answer) or answer.isnumeric()
    while not(is_number):
        print("The answer is not a number")
        answer = input("Please enter a number: ")
        is_number: bool = is_float(answer) or answer.isnumeric()

    if answer.isnumeric():
        response = int(answer)
    else:
        response = float(answer)

    if is_negative:
        return response * -1
    return response

def is_float(num: str) -> bool:
    try:
        converted = float(num)
        return int(converted) != converted
    except ValueError:
        return False

def parse_answer(question: str, chosen_symbol: str) -> Number:
    """
    Solves the answer for the given question. Division-based answers get
    rounded to 2 decimal places.
    
    Works for an operation between 2 numbers only
    """
    number1, number2 = [int(i) for i in question.split(chosen_symbol)]

    answer: Number
    if chosen_symbol == '+':
        answer = number1 + number2
    elif chosen_symbol == '-':
        answer = number1 - number2
    elif chosen_symbol == '*':
        answer = number1 * number2
    elif chosen_symbol == '/':
        answer = round(number1 / number2, 2)

        is_wholenumber = answer == int(answer)
        if is_wholenumber:
            answer = int(answer)

    return answer

def compare_answers(given_answer: Number, actual_answer: Number) -> bool:
    """
    Compares the two answers and tells the program whether they are the same
    or not
    """
    # Need to make a distinciton between floats and ints
    if type(actual_answer) == float:
        if type(given_answer) == int:
            return False
        given_answer = round(given_answer, 2)
    return actual_answer == given_answer

def show_time(user_time):
    user_time = f"{user_time:.2f}"
    print(f"Time taken: ", end='')
    colors.echo(user_time, colors.YELLOW, end='')
    print(" second(s)")

# Misc functions
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def leave_program(message):
    EXIT_CODE = { SUCCESS : 1, FAILURE : 0}[message]
    exit(EXIT_CODE)

# Import convention
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
if __name__ == "__main__":
    # For debugging and tests
    print(parse_answer("9 / 3", '/'))
    pass

