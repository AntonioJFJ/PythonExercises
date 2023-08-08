# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

valor = float(input('Digite o valor disponível (R$): '))
dólar = valor/3.27
print('Para o valor informado é possível comprar US$ {:.2f}'.format(dólar))
