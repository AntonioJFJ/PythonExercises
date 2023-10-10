# Vamos criar um menu em Python, usando modularização.
# Vamos ver como fazer acesso a arquivos usando o Python.
# Vamos finalizar o projeto de acesso a arquivos em Python.

from arquivo import *
from interface import *
from time import *
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Fechando o sistema. Volte sempre!')
        break
    else:
        print('\033[31mErro. Digite uma opção válida!\033[m')
    sleep(1)
