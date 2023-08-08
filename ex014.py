# Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.

temp = float(input('Digite o valor da temperatura (ºC): '))
f = (temp*1.8)+32
print('{} ºC corresponde a {} ºF'.format(temp, f))
