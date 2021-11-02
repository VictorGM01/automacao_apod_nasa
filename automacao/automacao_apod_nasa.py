from selenium import webdriver
from datetime import datetime
import smtplib
import email.message


navegador = webdriver.Chrome()
data = datetime.today()

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
    corpo_email = f"""
    <center>
        <h1>
            Foto de Hoje - NASA
        </h1>
    </center>
    <p>
        {data.day} de novembro de {data.year}
    </p>
    <p>
        <img src="{url_imagem}">
    </p>
    <p>
        {descricao}
    </p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Astronomia - Foto do Dia'
    msg['From'] = 'victormarques8801@gmail.com'



extrai_foto_do_site()
extrai_descricao_da_foto()