# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

print('Bem-vindo ao jogo do Robô 🤖')
print('-'*40)
número = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(número)
usuário = int(input('Escolha um número entre 0 e 5: '))
print('Carregando...')
time.sleep(1)
if usuário >5:
    print('Você escolheu um número maior que 5 🤦‍♂️')
elif usuário <0:
    print('Você escolheu um número menor que 0 🤦‍♂️')
elif usuário == sorteio:
    print('Parabéns 😀!\nVocê escolheu {} e a máquina também.'.format(usuário))
else:
    print('Infelizmente não foi dessa vez 😕\nVocê escolheu {} e a máquina {}.'.format(usuário, sorteio))
print('-'*40)
time.sleep(1)
print('Obrigado por jogar 🤖')
