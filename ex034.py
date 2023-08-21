# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Informe o salário atual (R$): '))
if salário > 1250:
    print('O salário reajustado será de R$ {:.2f}'.format(salário*1.10))
elif salário <= 0:
    print('Erro. Verifique o salário informado e tente novamente.')
else:
    print('O salário reajustado será de R$ {:.2f}'.format(salário*1.15))
