# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = homem = mulher_menor = 0

while True:
    idade = int(input('Qual sua idade? '))
    while idade < 0:
        idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual o seu sexo (Masculino/Feminino)? ')).lower().strip()[0]
    while sexo not in 'mf':
        sexo = str(input('Qual o seu sexo (Masculino/Feminino)? ')).lower().strip()[0]
    if idade > 18:
        maior = maior + 1
    if sexo in 'm':
        homem = homem + 1
    if sexo in 'f' and idade < 20:
        mulher_menor = mulher_menor + 1
    opção = str(input('Quer continuar (Sim/Não)? ')).lower().strip()[0]
    while opção not in 'sn':
        opção = str(input('Quer continuar (Sim/Não)? ')).lower().strip()[0]
    if opção in 'n':
        break
    print('-'*60)

if maior <= 1:
    print(f'\n\033[33m{maior} pessoa tem mais de 18 anos.\033[m')
else:
    print(f'\n\033[33m{maior} pessoas tem mais de 18 anos.\033[m')
if homem <= 1:
    print(f'\033[33m{homem} homem foi cadastrado.\033[m')
else:
    print(f'\033[33m{homem} homens foram cadastrados.\033[m')
if mulher_menor <= 1:
    print(f'\033[33m{mulher_menor} mulher tem menos de 20 anos.\033[m')
else:
    print(f'\033[33m{mulher_menor} mulheres tem menos de 20 anos.\033[m')
