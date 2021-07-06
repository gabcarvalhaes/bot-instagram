import colorama

from colorama import Fore
from colorama import Style

class Printer:    
    @staticmethod
    def error(message: str) -> None:
        colorama.init()
        print("\n" + Fore.RED + Style.BRIGHT + message + Style.RESET_ALL + "\n")
     
    @staticmethod   
    def primary(message: str) -> None:
        colorama.init()
        print("\n" + Fore.BLUE + Style.BRIGHT + message + Style.RESET_ALL + "\n")
        
    @staticmethod
    def success(message: str) -> None:
        colorama.init()
        print("\n" + Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL + "\n")

    @staticmethod
    def default(message: str) -> None:
        colorama.init()
        print("\n" + Style.BRIGHT + message + "\n")