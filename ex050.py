# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(1, 7):
    números = int(input('Digite o {}º número: '.format(c)))
    if (números%2) == 0:
        soma = soma + números
print('\033[33mA soma dos números pares é {}.\033[m'.format(soma))
