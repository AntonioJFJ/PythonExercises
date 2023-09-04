# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = média = maior = menor = 0

condição = 'S'
while condição in 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    condição = str(input('Você quer continuar? (S | N) ')).upper().strip()[0]

média = soma/cont
print('-'*40)
print('\n\033[33m{} números digitados e média entre eles igual a {:.2f}'.format(cont, média))
print('O maior valor foi {} e o menor {}.'.format(maior, menor))
