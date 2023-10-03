# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    área = largura * comprimento
    print('-' * 40)
    print(f'\033[36mPara a largura de {largura} m e comprimento de {comprimento} m, a área é {área:.2f} m².\033[m')


print('\033[33mCálculo de área\033[m'.center(40))
l = float(input('Digite a largura do terreno (m): '))
c = float(input('Digite o comprimento do terreno (m): '))
área(l, c)
