# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

import math
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
média = (nota1+nota2)/2
if 0.0 <= média < 5.0:
    print('\033[31mREPROVADO\nMédia = {:.2f}'.format(média))
elif 5.0 <= média < 7:
    print('\033[33mRECUPERAÇÃO\nMédia = {:.2f}'.format(média))
elif 7.0 <= média <= 10.0:
    print('\033[34mAPROVADO\nMédia = {:.2f}'.format(média))
else:
    print('\033[31mErro. Verifique as notas e tente novamente')

