# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

número = int(input('Informe um número: '))
print('Analisando o número {}'.format(número))
unidade = número//1 % 10
dezena = número//10 % 10
centena = número//100 % 10
milhar = número// 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
