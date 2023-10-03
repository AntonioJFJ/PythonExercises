# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

import random
números = []


def sorteia(lista):
    print('-'*60)
    while len(lista) < 5:
        pc = random.randint(1, 10)
        if pc not in lista:
            lista.append(pc)
    print(f'Os valores sorteados foram: \033[33m{sorted(lista)}\033[m')


def somaPar(pares):
    par = 0
    for n in pares:
        if (n % 2) == 0:
            par += n
    print(f'A soma entre os valores pares é: \033[33m{par}\033[m')
    print('-'*60)


sorteia(números)
somaPar(números)
