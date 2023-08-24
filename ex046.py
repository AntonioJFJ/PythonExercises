# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
print('\033[32mBem-vindo a queima de fogos do Ano Novo!\033[m')
time.sleep(1)
print('Preparem-se para a contagem regressiva.')
time.sleep(2)
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('Feliz Ano Novo! 🎆')
