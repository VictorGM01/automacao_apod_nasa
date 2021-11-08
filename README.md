# Automação - APOD NASA

## Descrição do Projeto
Automação do envio das imagens publicadas diariamente pela NASA, através do site APOD, aos e-mails predefinidos.

<h1 align="center">
    <img src="https://img.shields.io/github/license/VictorGM01/automacao_apod_nasa?style=for-the-badge"/>
    <img src="https://img.shields.io/static/v1?label=Linguagem&message=python&color=blue&style=for-the-badge&logo=PYTHON"/> 
    <img src="https://img.shields.io/static/v1?label=pip&message=21.3.0&color=purple&style=for-the-badge"/>
</h1>

### Funcionalidades :checkered_flag:
🚀 Busca a imagem do dia no site APOD, da NASA

:books: Traduz a explicação da imagem para português

:date: Verifica a data do dia da execução - útil para a edição do corpo do e-mail

:e-mail: Encaminha a Imagem, seu título e sua explicação traduzida aos e-mails definidos

### Demonstração da Aplicação
<p align="center"> Print do e-mail recebido no dia 7 de novembro de 2021 </p>
<h1 align="center">
  <img src="/assets/demonstracao.png" width="600" height="400"/>
</h1>

### Status :chart_with_upwards_trend:
Status do Projeto: concluído :heavy_check_mark:

### Pré Requisitos
Antes de começar, é preciso que você tenha instalado em sua máquina as seguintes ferramentas:

[Git](https://git-scm.com/), [Python](https://www.python.org/downloads/release/python-390/).

Além disso, é interessante que você tenha um editor para trabalhar com o código. Recomendo o uso do [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

### Como Rodar a Aplicação

```bash
# No terminal, clone este repositório:
git clone <https://github.com/VictorGM01/automacao_apod_nasa>

# Acesse a pasta do projeto
cd automacao_apod_nasa

# Instale as dependências
pip install ...

# Crie um arquivo chamado credencial.py

# Neste arquivo cria a constante SENHA e insira sua senha de aplicativos do gmail
- Caso você não tenha uma senha de aplicativo no gmail, entre no link https://support.google.com/accounts/answer/185839

# Abra o arquivo automacao_apod_nasa.py no Pycharm
 
# Com o editor de código aberto, modifique a variável "msg['From']", inserindo seu e-mail

# Edite a variável "msg['To']" com o e-mail de destinatário

# Após seguir as etapas anteriores, rode o código pelo editor, ou pelo terminal, da seguinte maneira:
automacao_apod_nasa.py

````
