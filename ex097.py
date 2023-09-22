# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(txt):
    print()
    print('~'*len(mensagem))
    print(f'\033[36m{mensagem}\033[m'.ljust(len(mensagem)))
    print('~'*len(mensagem))


mensagem = str(input('Digite qualquer frase: '))
escreva(mensagem)
