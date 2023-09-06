# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('\033[36m=\033[m'*60)
print('\033[1:33mTonico Mall\033[m'.center(60))
print('\033[36m=\033[m'*60)
total = acima_mil = contador = mais_barato = 0
nome_barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$ '))
    total += preço
    if preço > 1000:
        acima_mil += 1
    if contador == 0:
        mais_barato = preço
        nome_barato = nome
    else:
        if preço < mais_barato:
            mais_barato = preço
            nome_barato = nome
    contador += 1
    opção = str(input('Deseja continuar [S/N]? ')).lower().strip()[0]
    while opção not in 'sn':
        opção = str(input('Deseja continuar [S/N]? ')).lower().strip()[0]
    print('-' * 60)
    if opção == 'n':
        break

print(f'\033[33mO total gasto na compra foi R$ {total:.2f}\033[m')
print(f'\033[33m{acima_mil} produto(s) acima de R$ 1000.00\033[m')
print(f'\033[33mO produto mais barato foi o(a) {nome_barato}\033[m')
