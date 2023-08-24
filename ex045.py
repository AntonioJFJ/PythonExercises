# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
print('\033[1:43mBem-Vindo ao Jokenpô Game ✊ ✋ ✌️\033[m'.center(100))
time.sleep(1)
apresentação = int(input('Preparado para jogar?\n[1] Sim\n[2] Não\n'))
if apresentação == 1:
    print('Aí sim, bora lá então! 😎')
elif apresentação == 2:
    print('ih, vai arregar? 🐓')
    time.sleep(1)
    print('Para de graça e vamos nessa.')
else:
    print('Tá loucão?\nPresta atenção nas opções! 🥴')
    exit()
time.sleep(1)
print('-'*100)
nome = str(input('Escreva seu nick name: '))
time.sleep(1)
print('{}, vou te explicar como o jogo funciona:\n'
      '\n✊: Pedra | ✋: Papel | ✌️: Tesoura\n'
      
      '\n✊ GANHA ✌️'
      '\n✌️ GANHA ✋'
      '\n✋ GANHA ✊\n'
      
      '\nMãos iguais = EMPATE'.format(nome))
print('-'*100)
time.sleep(3)

# [1] Pedra
# [2] Papel
# [3] Tesoura

opções = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
print('Agora vou escolher uma MÃO e você faça o mesmo, no 3 a gente mostra o que escolheu.')
usuário = int(input('Escolha uma das opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n'))
if 0 <= usuário <= 2:
    print('OK. Opção {}\n'.format(usuário))
else:
    print('Tá loucão?\nPresta atenção nas opções! 🥴')
    exit()
print('1, ', end='')
time.sleep(1)
print('2, ', end='')
time.sleep(1)
print('3.')
time.sleep(1)
if pc == usuário:
    print('\033[33mIxi, deu EMPATE. Bora jogar de novo 🤨\033[m\n'
          'Eu escolhi {} e você {}'.format((opções[pc]), (opções[usuário])))
elif (pc == 0 and usuário == 2) or (pc == 2 and usuário == 1) or (pc == 1 and usuário == 0):
    print('Eu escolhi {} e você {}'.format((opções[pc]), (opções[usuário])))
    print('\033[31mO Computador venceu 🤖\033[m')
else:
    print('Eu escolhi {} e você {}'.format((opções[pc]), (opções[usuário])))
    print('\033[32mVocê venceu 👨‍💻\033[m')
