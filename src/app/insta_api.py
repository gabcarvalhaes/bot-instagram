import sys

from instaloader import instaloader
from instaloader.nodeiterator import NodeIterator
from instaloader.structures import Profile

from src.app.printer import Printer
from src.app.user import User

class InstaAPI:
    # * Inicializa a classe Instaloader e autentica o usuário com a API
    def __init__(self, user: User) -> None:
        self.insta_loader = instaloader.Instaloader()
        self.user = user
        
        try:
            self.insta_loader.login(self.user.username, self.user.password)
        except Exception as error:
            Printer.error(error)
            sys.exit()

    # * Retorna todas as contas a quem o usuário logado segue
    def get_followees(self) -> NodeIterator[Profile]:
        try:
            profile = instaloader.Profile.from_username(self.insta_loader.context, self.user.username)

            return profile.get_followees()
        except Exception as error:
            Printer.error(error)
            sys.exit()
        