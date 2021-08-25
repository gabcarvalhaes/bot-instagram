import time
import os
import sys
import colorama
import random

from getpass import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from instaloader.nodeiterator import NodeIterator
from instaloader.structures import Profile

from src.app.insta_api import InstaAPI
from src.app.printer import Printer
from src.app.user import User

class Bot:
    INSTAGRAM_URL = 'https://www.instagram.com' # * Url padrão do Instagram
    EDGE_DRIVER = '/src/drivers/msedgedriver.exe' # * Driver do Microsoft Edge
    

    def __init__(self) -> None:
        colorama.init()

        self.user = None

    # * Recebe e armazena as credenciais do usuário
    def credentials(self) -> None:
        username = str(input('Login/Usuário do Instagram: '))
        password = str(getpass('Senha: '))

        self.user = User(username, password)

    # * Filtra os usuários e os retorna dentro de uma nova lista
    def filter_users(self, users_list: NodeIterator[Profile], profile_page: str) -> list:
        new_users_list = []

        for user in users_list:
            if 'dix' not in user.username and 'oficial' not in user.username and 'official' not in user.username and user.username != profile_page and user.is_verified != True:
                new_users_list.append('@' + user.username)
        
        return new_users_list

    def run(self) -> None:
        self.credentials()        

        # * Informações para a operação
        profile_page = str(input('Perfil do sorteador: '))
        url = str(input('Página do sorteio: '))
        person_numbers = int(input('Número de pessoas a marcar por comentário: '))
        comment = str(input('Comentário: '))

        Printer.primary('Aguarde... abrindo navegador.')
        time.sleep(2)

        # * Instanciar o drive do navegador
        browser = webdriver.Edge(os.getcwd() + self.EDGE_DRIVER)

        # * Abre a página do Instagram
        browser.get(self.INSTAGRAM_URL)

        time.sleep(2)

        # * Busca pelo campo username e digita o nome do usuário
        username_input = browser.find_element_by_name('username')
        username_input.send_keys(self.user.username)

        # * Busca pelo campo password e digita a senha
        password_input = browser.find_element_by_name('password')
        password_input.send_keys(self.user.password)

        # * Busca pelo botão de login e faz o submit
        login_submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
        login_submit_button.submit()

        time.sleep(2)

        # * Verifica se há erro no login
        try:
            login_error = browser.find_element_by_id('slfErrorAlert')

            # * Caso exista erro, o programa irá apresentar a mensagem e finalizar a operação
            if login_error:
                Printer.error(login_error.text)
                sys.exit()

        # * Caso não tenha encontrado o erro, o login foi efetuado com sucesso!
        except NoSuchElementException:
            Printer.success('Login efetuado com sucesso!')
            pass

        insta_api = InstaAPI(self.user)

        time.sleep(2)

        # * Busca o botão "Agora não" para Salvar Informações e avançar a página
        pass_button = browser.find_elements_by_tag_name('button')[1]
        pass_button.click()

        Printer.primary('Aguarde...')
        time.sleep(2)

        # * Busca o botão "Agora não" para Notificação e avançar a página
        pass_button = browser.find_element_by_xpath('//div[@class="mt3GC"]/button[1]')
        pass_button.click()

        # * Lista de usuários tratados
        users_list = self.filter_users(insta_api.get_followees(), profile_page)

        index = 0
        index2 = 0
        index3 = 0
        comments_list = ['' for x in range(int(len(users_list) / person_numbers))] # * Cria espaços vazios para os comentários dentro de um array

        # * Filtra e adiciona os usuários corretamente nesses arrays
        while index < int(len(users_list) / person_numbers):
            while index2 < person_numbers:                
                comments_list[index] += users_list[index3 + index2] + ' '

                index2 += 1

                if index2 >= person_numbers:
                    comments_list[index] += comment
                    index3 += person_numbers

            index2 = 0
            index += 1

        Printer.primary('Aguarde... abrindo página do sorteio')
        time.sleep(2)

        browser.get(url)

        time.sleep(4)
        Printer.primary('Iniciando operação... aguarde')

        index = 0

        # * Realiza os comentários com as marcações nas publicações
        while index < len(comments_list):    
            browser.find_element_by_class_name('Ypffh').click()
            comment_field = browser.find_element_by_class_name('Ypffh')
            comment = comments_list[index]

            Printer.primary(comment + ' -> ' + index)
                
            for letter in comment:
                comment_field.send_keys(letter)
                time.sleep(random.randint(1, 5) / 30)

            time.sleep(random.randint(30, 150))

            publicate_button = browser.find_element_by_xpath('//button[@type="submit"]')
            publicate_button.click()

            index += 1
            Printer.primary('Próximo...')
            
            time.sleep(5)
        else:
            Printer.primary('Finalizando operação')

            time.sleep(3)
            sys.exit()




