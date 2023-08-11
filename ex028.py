# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

número = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(número)
usuário = int(input('Escolha um número entre 0 e 5: '))
if usuário == sorteio:
    print('Parabéns 😀!\nVocê escolheu {} e a máquina também.'.format(usuário))
else:
    print('Infelizmente não foi dessa vez 😕. Você escolheu {} e a máquina {}'.format(usuário, sorteio))
print('Obrigado por jogar 🤖')
