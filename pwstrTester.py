import string
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

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
specialCase = string.punctuation
numberCase = "1234567890"

def userInput():
    while True:
        userPassword = input(f"{Colors.BLUE}Create a password: {Colors.RESET}")
        
        hasLower = any(char in lowerCase for char in userPassword)
        hasUpper = any(char in upperCase for char in userPassword)
        hasSpecial = any(char in specialCase for char in userPassword)
        hasNumber = any(char in numberCase for char in userPassword)

        if len(userPassword) == 0:
            print(f"{Colors.RED}You cannot create an empty password!{Colors.RESET}")
            continue

        if not hasUpper:
            print(f"{Colors.RED}ERROR: Add uppercase letter(s){Colors.RESET}")
        if not hasLower:
            print(f"{Colors.RED}ERROR: Add lowercase letter(s){Colors.RESET}")
        if not hasSpecial:
            print(f"{Colors.RED}ERROR: Add special character(s){Colors.RESET}")
        if not hasNumber:
            print(f"{Colors.RED}ERROR: Add number(s){Colors.RESET}")
            
        if hasUpper and hasLower and hasSpecial and hasNumber and len(userPassword) >= 8:
            print(f"{Colors.GREEN}Excellent password!{Colors.RESET}")
            exitInput()
            break

        if len(userPassword) <= 7:
            print(f"{Colors.RED}You're password MUST be 8 characters or longer!{Colors.RESET}")
            continue
              
def exitInput():
    while True:
        continueInput = input(f"{Colors.YELLOW}Continue(Y or N): {Colors.RESET}")

        inputA = "Y", "y"
        inputB = "N", "n"

        if continueInput in inputA:
            userInput()
            break
        elif continueInput in inputB: 
            sys.exit()
        else: print("Fail")

print(f"{Colors.GREEN}Hello user!{Colors.RESET}")
print(f"{Colors.YELLOW}Welcome to Password Strength Tester{Colors.RESET}")
userInput()