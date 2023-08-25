# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    if (num%c) == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if cont == 2:
    print('\n\033[32mO número {} É primo\033[m, pois só é divisível por 1 e por ele mesmo.'.format(num))
else:
    print('\n\033[31mO número {} NÃO é primo\033[m.'.format(num))
