# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('O carro foi alugado por quantos dias?\n'))
km = float(input('Quantos km foram percorridos com o carro?\n'))
custo = (dias*60)+(0.15*km)
print('O preço a ser pago será de R$ {:.2f}'.format(custo))
