from selenium import webdriver
import time
import smtplib
import email.message


navegador = webdriver.Chrome()

def extrai_foto_do_site():
    navegador.get('https://apod.nasa.gov/apod/astropix.html')
    navegador.find_element('xpath', '/html/body/center[1]/p[2]/a/img').click()

    global url_imagem
    url_imagem = navegador.current_url


def extrai_descricao_da_foto():
    navegador.get('https://apod.nasa.gov/apod/astropix.html')

    global descricao
    descricao = navegador.find_element(by='xpath', value='/html/body/p[1]').text


def encaminha_email():
    pass


extrai_descricao_da_foto()