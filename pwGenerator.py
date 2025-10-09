import random
import string
import secrets
import sys
from pathlib import Path

class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    RESET = "\033[0m"

randomChar = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
   
def generateRandomPassword():
    passwordLength = random.randint(8, 24)
    passwordRandom = ''.join(secrets.choice(randomChar) for _ in range(passwordLength))
    print(f"{Colors.MAGENTA}{passwordRandom}{Colors.RESET}")
    return passwordRandom

def saveContinueExit():
    result = generateRandomPassword()
    
    print(f"{Colors.GREEN}[1] Continue{Colors.RESET}")
    print(f"{Colors.CYAN}[2] Save Password{Colors.RESET}")
    print(f"{Colors.RED}[3] Exit{Colors.RESET}")

    userInput = int(input(f"{Colors.YELLOW}Enter option (1/2/3): {Colors.RESET}"))

    inputA = 1
    inputB = 2
    inputC = 3

    if userInput == inputA:
        saveContinueExit()

    elif userInput == inputB:
        fileDirectory = Path.cwd() 
        with open("password.txt", "w") as file:
            file.write(result)
        print(f"{Colors.GREEN}Saved{Colors.RESET} {result} in {Colors.GREEN}{fileDirectory}{Colors.RESET}")
        saveContinueExit()

    elif userInput == inputC:
        sys.exit()

    else: 
        userInput != inputA or inputB or inputC
        print("Error!")
        saveContinueExit()

def mainMenu():
    print(f"{Colors.CYAN}Password Generator{Colors.RESET}")
    print(f"{Colors.GREEN}[1] Generate Random Password (8-24){Colors.RESET}")
    print(f"{Colors.RED}[2] Exit{Colors.RESET}")

    userInput = int(input(f"{Colors.YELLOW}Enter option (1/2): {Colors.RESET}"))

    inputA = 1
    inputB = 2

    if userInput == inputA:
        saveContinueExit()

    if userInput == inputB:
        sys.exit()

mainMenu()