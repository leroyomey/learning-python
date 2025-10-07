import random
import string
import secrets
import sys

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

def generatePassword():
    userInput = int(input("Enter a password length: "))
    password = ''.join(secrets.choice(randomChar) for _ in range(userInput))
    print(password)

def generateRandomPassword():
    passwordLength = random.randint(8, 24)
    passwordRandom = ''.join(secrets.choice(randomChar) for _ in range(passwordLength))
    print(passwordRandom)

def continueOrExit():
    userInput = input(f"{Colors.YELLOW}Continue? (y/n): {Colors.RESET}")

    inputA = "y", "Y"
    inputB = "n", "N"

    if userInput in inputA:
        generateRandomPassword()
        continueOrExit()
    elif userInput in inputB:
        sys.exit()
    else: 
        print(f"{Colors.RED}Error!{Colors.RESET}")
        continueOrExit()

def generateMethod():
    print(f"{Colors.CYAN}Password Generator{Colors.RESET}")
    print(f"{Colors.GREEN}[1] Generate Random Password (8-24){Colors.RESET}")
    print(f"{Colors.RED}[2] Exit{Colors.RESET}")

    userInput = int(input(f"{Colors.YELLOW}Enter option (1/2): {Colors.RESET}"))

    if userInput == 1:
        generateRandomPassword()
        continueOrExit()
    if userInput == 2:
        sys.exit()
    else: pass

generateMethod()