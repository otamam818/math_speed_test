# Imports
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
import sys
import math_handler

# Constants
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
# | CLI Arguments
GENERATE_COMMAND: str = '-g'
ADDITION:         str = '-a'
SUBTRACTION:      str = '-s'
DIVISION:         str = '-d'
MULTIPLICATION:   str = '-m'

# | Error Messages
MESSAGE_IndexError = """
Wrong format. Please use The following format:,
python3 cli.py -g NUMBER -x,
Where -x could be any of the following operators: ,
   -a -> addition,
   -s -> subtraction,
   -m -> multiplication,
   -d -> division
"""

# | File names
FILE_PREVIOUS_CALCULATIONS: str = "../../data/previous_calculations.txt"
FILE_LAST_CALCULATION:      str = "../../data/.last_calculation"
FILE_TEMP_USER_SCORE:       str = "../../data/.usr_score"

ALL_FILES: list = [
    FILE_LAST_CALCULATION,
    FILE_PREVIOUS_CALCULATIONS,
    FILE_TEMP_USER_SCORE
]

# Main function
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
def main(argv: list):
    """Is mainly used from the command line for invoking"""
    try:
        parse_commands(argv)
    except IndexError:
        print(MESSAGE_IndexError)
        exit()

def parse_commands(argv: list) -> None:
    """
    Parses the commands to generate mathematical questions based on
    requirements
    """
    command = argv[1]

    # We need to know for how many digits we need to calculate
    num_calc_digits: int = int(argv[2])

    # To know which math operation to call
    calc_type: int = argv[3]

    # For mapping command-line operations with their math operators
    operator_dict = {
        ADDITION       : '+',
        SUBTRACTION    : '-',
        MULTIPLICATION : '*',
        DIVISION       : '/'
    }

    if command == GENERATE_COMMAND:
        question: str = math_handler.rand_math_question(
            num_calc_digits, 
            operator_dict[calc_type]
        )

        # Log the data for other (faster) languages to access
        for my_file in ALL_FILES:
            record_calculation(my_file, question)

        # As a CLI, the print acts as a return value
        print(question)

def record_calculation(filename: str, data: str) -> None:
    """Records the calculation that took place"""
    mode: str
    if filename == FILE_PREVIOUS_CALCULATIONS:
        mode = 'a'
        data += '\n'
    else:
        mode = 'w'

    with open(filename, mode) as my_file:
        my_file.write(data)

# Import convention
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
if __name__ == "__main__":
    main(sys.argv)

