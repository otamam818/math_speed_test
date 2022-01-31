import random

def rand_math_question(num_digits: int, operator) -> str:
    number1 = random.randint(0, num_digits)

    # We don't want zero division or a simple calculation
    number2 = random.randint(2, num_digits)
    return f"{number1} {operator} {number2}"

