# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

import time
def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('-='*40)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
    if início < fim:
        for c in range(início, fim+1, passo):
            time.sleep(0.4)
            print(f'\033[33m{c}\033[m', end=' ')
    elif fim < início:
        for c in range(início, fim-1, passo*(-1)):
            time.sleep(0.4)
            print(f'\033[33m{c}\033[m', end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*40)
print('\033[35mAgora é sua vez. Defina o início, fim e passo da P.A.\033[m')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
