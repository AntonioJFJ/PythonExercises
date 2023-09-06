# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('\033[36m=\033[m'*60)
print('\033[1:32m$ Tonhão Bank $\033[m'.center(60))
print('\033[36m=\033[m'*60)
nota50 = nota20 = nota10 = nota1 = 0
resto50 = resto20 = resto10 = resto1 = 0

print('\nSaque conta-corrente')
print('\033[33mCédulas disponíveis -> R$50, R$20, R$10, R$1\033[m\n')
print('-'*60)
valor = int(input('Informe o valor do saque: R$ '))
while True:
    nota50 = valor // 50
    resto50 = valor % 50
    if resto50 == 0:
        break
    else:
        nota20 = resto50 // 20
        resto20 = resto50 % 20
        if resto20 == 0:
            break
        else:
            nota10 = resto20 // 10
            resto10 = resto20 % 10
            if resto10 == 0:
                break
            else:
                nota1 = resto10 // 1
                resto1 = resto10 % 1
                break
print('-'*60)

if nota50 >= 1:
    print(f'\n\033[32m{nota50} cédula(s) de R$ 50\033[m')
if nota20 >= 1:
    print(f'\033[32m{nota20} cédula(s) de R$ 20\033[m')
if nota10 >= 1:
    print(f'\033[32m{nota10} cédula(s) de R$ 10\033[m')
if nota1 >= 1:
    print(f'\033[32m{nota1} cédula(s) de R$ 1\033[m')
