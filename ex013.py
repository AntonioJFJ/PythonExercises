# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Informe o salário atual (R$): '))
novo = s*1.15
print('O salário reajustado é de R$ {:.2f}'.format(novo))
