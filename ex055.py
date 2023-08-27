# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range(1, 6):
    print('{}ª pessoa'.format(c))
    peso = float(input('Digite seu peso (kg): '))
    print('-'*40)
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR peso é {} kg e o MENOR é {} kg.'.format(maior, menor))
