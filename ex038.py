# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

import time
num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite outro número: '))
print('Carregando...')
time.sleep(1)
if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('\033[31mNão existe valor maior, os dois números são iguais.')
