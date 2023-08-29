# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

cont = 1
import time
import random
print('\033[4:33m-Bem-vindo ao jogo da adivinhação-\n\033[m'.center(100))
person = int(input('Escolha um número entre 0 e 10:\n'))
pc = random.randint(0, 10)

while pc != person:
    person = int(input('\033[31mErrou.\nVai tentando aí...\n\033[m'.format(pc, person)))
    cont += 1

print('\033[32mAté que enfim acertou\033[m\nEu pensei no {} e você também pensou no {}.\nVocê tentou {} vezes.'
      .format(pc, person, cont))
