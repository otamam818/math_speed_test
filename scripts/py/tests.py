# Standard library imports
import unittest, subprocess
from typing import List

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

