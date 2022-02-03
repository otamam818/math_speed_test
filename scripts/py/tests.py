# Standard library imports
import unittest, subprocess
from typing import List
from random import choice

# Local imports
import json_handler, interface, math_handler, cli

def main():
    unittest.main()

class TestScripts(unittest.TestCase):
    # Module: math_handler.py
    def test_rand_math_question(self):
        symbol   :  str = '+'
        question :  str = math_handler.rand_math_question(100, symbol)
        numbers  : List[str] = [i.strip() for i in question.split(symbol)]

        self.assertTrue(all_numeric(numbers))

    # Module: cli.py
    def test_parse_commands(self):
        option = 1000
        symbol_arg = interface.get_symbol_arg()
        command = f"python3 cli.py -g {option} {symbol_arg}"
        result = subprocess.getoutput(command)
        components: list = result.split()
        
        # Check if the positioning of the result is correct
        are_numbers: bool = components[0].isnumeric()
        are_numbers = are_numbers and components[2].isnumeric()
        is_symbol: bool = components[1] in interface.SYMBOLS
        is_valid: bool = are_numbers and is_symbol

# Helper functions
def all_numeric(iterable: List[str]) -> bool:
    """check if they are all numeric"""
    # We want to know whether every string within is a number
    number_string: str 
    for number_string in iterable:
        if not(number_string.isnumeric()): 
            return False

    return True

if __name__ == "__main__":
    main()

