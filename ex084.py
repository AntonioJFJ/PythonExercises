# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dado = []
pesado = leve = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso (kg): ')))
    if len(lista) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        if dado[1] < leve:
            leve = dado[1]
    lista.append(dado[:])
    dado.clear()
    opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    while opção not in 'sn':
        opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    if opção in 's':
        continue
    elif opção in 'n':
        break

print(f'\n\033[33mForam cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi {pesado:.2f} kg. -> Nome(s): ', end='')
for p in lista:
    if p[1] == pesado:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {leve:.2f} kg. -> Nome(s): ', end='')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}]', end='')
print()
