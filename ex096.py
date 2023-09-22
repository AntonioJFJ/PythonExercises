# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def área(a, b):
    s = a * b
    print('-' * 40)
    print(f'\033[36mPara a largura de {a} m e comprimento de {b} m, a área é {s:.2f} m².\033[m')


print('\033[33mCálculo de área\033[m'.center(40))
a = float(input('Digite a largura do terreno (m): '))
b = float(input('Digite o comprimento do terreno (m): '))
área(a, b)
