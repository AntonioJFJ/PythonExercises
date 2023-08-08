# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Informe o preço do produto (R$): '))
d = p*0.95
print('O valor do produto com desconto de 5% é R$ {:.2f}'.format(d))
