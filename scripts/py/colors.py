import subprocess

RED    = "$(tput setaf 2)"
GREEN  = "$(tput setaf 6)"
BLUE   = "$(tput setaf 3)"
YELLOW = "$(tput setaf 1)"
RESET  = "$(tput setaf 10)"

def echo(text: str, color: str, end: str = '\n') -> None:
    """Prints with colored text"""
    toprint = subprocess.getoutput(f'echo "{color}{text}{RESET}"')
    print(toprint, end=end)

