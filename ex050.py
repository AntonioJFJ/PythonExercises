# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for c in range(1, 7):
    números = int(input('Digite o {}º número: '.format(c)))
    if (números%2) == 0:
        cont = cont + 1
        soma = soma + números
print('\033[33m{} número(s) par(es) e sua soma é igual a {}.\033[m'.format(cont, soma))


#soma += números
#cont += 1