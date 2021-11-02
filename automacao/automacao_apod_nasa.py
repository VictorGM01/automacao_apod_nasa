from selenium import webdriver
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from translate import Translator

from credencial import SENHA


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


def traduz_descricao_da_foto():
    tradutor = Translator(from_lang="English", to_lang="Portuguese")
    global descricao_traduzida
    descricao_traduzida = tradutor.translate(descricao)


def encaminha_email():
    corpo_email = f"""
    <html>
        <head></head>
        <body>
            <center>
                <h1>
                    Foto de Hoje - NASA
                </h1>
                <p>
                    {data.day} de novembro de {data.year}
                </p>
                <p>
                    <img src="{url_imagem}" width="600" height="300">
                </p>
            </center>
            <p>
                Descrição da Imagem:
                {descricao_traduzida}
                
            </p>
            <p>
                Descrição (Inglês)
                {descricao}
            </p>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['Subject'] = 'Astronomia - Foto do Dia'
    msg['From'] = 'victormarques8801@gmail.com'
    msg['To'] = 'victormarques8801@gmail.com'
    msg.attach(MIMEText(corpo_email, 'html'))

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()
    s.starttls()
    s.login(msg['From'], SENHA)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


extrai_foto_do_site()
extrai_descricao_da_foto()
encaminha_email()