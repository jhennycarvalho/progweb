from flask import Flask

meu_site = Flask(__name__)

@meu_site.route("/")
def inicio():
    return "Olá! Meu primeiro projeto Flask!"

@meu_site.route('/contato')
def contato():
    return 'numero: 69984258688'

def saudacoes(nome):
    return f'ola {nome}.'

@meu_site.route('/saudacao/<nome>')
def saudacao (nome):
    return saudacoes(nome)

meu_site.run(port=8000)

