# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*40)
print('\033[1mSequência de Fibonacci\033[m'.center(40))
print('-'*40)
termos = int(input('Quantos termos você quer mostrar?\n'))

t1 = 0
t2 = 1
cont = 3
print('{} - {}'.format(t1, t2), end='')
while cont <= termos:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' - Fim')

