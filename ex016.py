# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

import math
n = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é {}'.format(n, math.trunc(n)))
# Obs: trunc e floor não são equivalentes.
