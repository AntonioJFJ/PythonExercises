# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

import math
num = int(input('Digite um número inteiro qualquer: '))
base = int(input('Escolha a base de conversão:\n1 Binário | 2 Octal | 3 Hexadecimal\n'))
binário = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if base == 1:
    print('{} em binário é {}.'.format(num, binário[2:]))
elif base == 2:
    print('{} em octal é {}.'.format(num, octal[2:]))
elif base == 3:
    print('{} em hexadecimal é {}.'.format(num, hexadecimal[2:]))
else:
    print('Erro. Escolha a base de conversão de acordo com as opções!')

# Não esquecer de utilizar fatiamento para esconder os caracteres indesejados.
