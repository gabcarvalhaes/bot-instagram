class Printer:    
    @staticmethod
    def error(message: str) -> None:
        print("\n \033[1;31m" + message + "\n")
     
    @staticmethod   
    def primary(message: str) -> None:
        print("\n \033[0;32m" + message + "\n")
        
    @staticmethod
    def success(message: str) -> None:
        print("\n \033[1;36m" + message + "\n")

    @staticmethod
    def default(message: str) -> None:
        print("\n \033[0;0m " + message + "\n")