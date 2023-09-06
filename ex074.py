# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
cont = menor = maior = 0
for tupla in range(0, 5):
    aleatório = random.randint(1, 10)
    cont = cont + 1
    print(aleatório, end=' ')
    if cont == 1:
        menor = aleatório
        maior = aleatório
    else:
        if aleatório < menor:
            menor = aleatório
        if aleatório > maior:
            maior = aleatório

print(f'\n\033[33mO menor número é {menor}')
print(f'O maior número é {maior}\033[m')
