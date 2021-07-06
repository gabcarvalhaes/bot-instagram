from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from printer import Printer
from getpass import getpass

import time
import os

INSTAGRAM_URL = 'https://www.instagram.com' # * Url padrão do Instagram
USERS_TXT = 'src/users.txt' # * Arquivo txt de usuários
EDGE_DRIVER = '/drivers/msedgedriver.exe' # * Driver do Microsoft Edge

# * Solicita o usuário e senha
username = str(input('Login/Usuário do Instagram: '))
password = str(getpass('Senha: '))

page = str(input('Perfil do sorteador: '))
url = str(input('Página do sorteio: '))
person_numbers = int(input('Número de pessoas a marcar por comentário: '))
comment = str(input('Comentário: '))

Printer.primary('Aguarde... abrindo navegador.')
time.sleep(2)

# * Instanciar o drive do navegador
driver = os.getcwd() + EDGE_DRIVER
browser = webdriver.Edge(driver)

# * Abre a página do Instagram
browser.get(INSTAGRAM_URL)

time.sleep(2)

# * Busca pelo campo username e digita o nome do usuário
username_input = browser.find_element_by_name('username')
username_input.send_keys(username)

# * Busca pelo campo password e digita a senha
password_input = browser.find_element_by_name('password')
password_input.send_keys(password)

# * Busca pelo botão de login e faz o submit
login_submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
login_submit_button.submit()

time.sleep(2)

# * Verifica se há erro no login
try:
    login_error = browser.find_element_by_id('slfErrorAlert')

    if login_error:
        Printer.error(login_error.text)

# * Caso não tenha encontrado o erro, o login foi efetuado com sucesso!
except NoSuchElementException as error:
    Printer.success('Login efetuado com sucesso!')
    pass

time.sleep(2)

# * Busca o botão "Agora não" para Salvar Informações e avançar a página
pass_button = browser.find_elements_by_tag_name('button')[1]
pass_button.click()

Printer.primary('Aguarde...')
time.sleep(2)

# * Busca o botão "Agora não" para Notificação e avançar a página
pass_button = browser.find_element_by_xpath('//div[@class="mt3GC"]/button[1]')
pass_button.click()

# * Realiza a leitura do arquivo TXT de usuários
users_list = open(USERS_TXT, 'r').read().split()

index = 0
new_users_list = [[] for x in range(int(len(users_list) / person_numbers))] # * Cria arrays vazios dentro de um array

# * Filtra e adiciona os usuários corretamente nesses arrays
# todo: Verificar criação dos arrays vazios que estão sobrando
for user in users_list:
    if 'dix' not in user and 'oficial' not in user and 'official' not in user:
        username = '@' + str(user).strip()
        new_users_list[index].append(username)

    if len(new_users_list[index]) == person_numbers:
        index += 1

# todo: Realizar os comentários com as marcações nas publicações
for users_to_comments in new_users_list:
    pass    