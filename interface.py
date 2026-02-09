from colorama import Fore, Style

def get_user_input():
    print(Fore.GREEN + "\nВы: ", end="")
    return input(Style.RESET_ALL).strip()

def print_header():
    print(Fore.MAGENTA + "\n" + "="*30)
    print(Fore.MAGENTA + "   AKYLMAN AI SYSTEM V2.0")
    print(Fore.MAGENTA + "="*30 + "\n")
