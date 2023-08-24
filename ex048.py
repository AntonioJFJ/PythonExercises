# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

cont = 0
soma = 0
for n in range(1, 501, 2):
    if (n%3) == 0:
        cont = cont + 1
        soma = soma + n
print('O somatório dos \033[33m{}\033[m valores ímpares e múltiplos de 3 no intervalo de 1 a 500 é: \033[4:33m{}'.format(cont, soma))

