from text_style import TextStyle

class Printer:
    
    def error(message: str) -> None:
        print(TextStyle.ERROR + "\n" + message + "\n")
        
    def primary(message: str) -> None:
        print(TextStyle.PRIMARY + "\n" + message + "\n")
        
    def success(message: str) -> None:
        print(TextStyle.SUCCESS + "\n" + message + "\n")

    def default(message: str) -> None:
        print(TextStyle.DEFAULT + "\n" + message + "\n")