from selenium import webdriver
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

from credencial import SENHA


navegador = webdriver.Chrome()
data = datetime.today()

def extrai_foto_do_site():
    navegador.get('https://apod.nasa.gov/apod/astropix.html')

    global titulo
    titulo = navegador.find_element('xpath', '/html/body/center[2]/b[1]').text

    navegador.find_element('xpath', '/html/body/center[1]/p[2]/a/img').click()

    global url_imagem
    url_imagem = navegador.current_url


def extrai_descricao_da_foto():
    navegador.get('https://apod.nasa.gov/apod/astropix.html')

    global descricao
    descricao = navegador.find_element(
        by='xpath', value='/html/body/p[1]').text


def traduz_descricao_da_foto():
    navegador.get('https://translate.google.com.br/?hl=pt-BR')
    box =\
        navegador.find_element('xpath',
                               '//*[@id="yDmH0d"]/c-wiz/div/div[2]/' +
                               'c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/' +
                               'c-wiz[1]/span/span/div/textarea')
    box.click()
    box.send_keys(descricao)

    time.sleep(20)
    global descricao_traduzida
    descricao_traduzida = \
        navegador.find_element('xpath',
                               '//*[@id="yDmH0d"]/c-wiz/div/div[2]/' +
                               'c-wiz/div[2]/c-wiz/div[1]/div[2]/' +
                               'div[2]/c-wiz[2]/div[5]/div/div[1]').text


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
                    Esta foto foi retirada do site oficial da NASA,
                    chamado APOD, onde todos os dias uma foto/imagem
                    relacionada à astronomia é publicada
                </p>
                <p>
                    {data.day} de novembro de {data.year}
                </p>
                <p>
                    <img src="{url_imagem}" width="600" height="300">
                </p>
                <h3> {titulo} </h3>
            </center>
            <p>
                {descricao_traduzida}
            </p>
            <p>E-mail enviado automaticamente usando o Python :)</p>
        </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['Subject'] = f'Foto do Dia {data.day} - NASA'
    msg['From'] = 'victormarques8801@gmail.com'
    msg['To'] = 'victormarques8801@gmail.com'
    msg.attach(MIMEText(corpo_email, 'html'))

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()
    s.starttls()
    s.login(msg['From'], SENHA)
    s.sendmail(msg['From'], [msg['To'], 'raphaelagferraz2@gmail.com'],
               msg.as_string().encode('utf-8'))

    print('-------------------------------------------------------')
    print('Email enviado com sucesso aos destinatários informados!')
    print('-------------------------------------------------------')


extrai_foto_do_site()
extrai_descricao_da_foto()
traduz_descricao_da_foto()
encaminha_email()