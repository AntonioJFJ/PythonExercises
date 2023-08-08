# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
b = float(input('Informe o comprimento do cateto oposto (cm): '))
c = float(input('Informe o comprimento do cateto adjacente (cm): '))
a = math.sqrt((pow(b, 2))+(pow(c, 2)))
# Na linha acima foi utilizado 'pow' apenas para praticar.
# math.hypot(b, c) também gera o mesmo resultado de 'a'.
print('Tendo o cateto oposto igual a {} e o adjacente igual a {}, a hipotenusa é {} cm'.format(b, c, a))
