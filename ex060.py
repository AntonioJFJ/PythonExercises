# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para visualizar seu fatorial: '))
c = num
soma = 0
while c > 0:
    print(c)
    c -= 1
    mult = num*c
    soma += mult
print('{}! = {}'.format(num, mult))



# forma fácil:
'''from math import fatorial
num = int(input('Digite um número para visualizar seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num, f))
'''