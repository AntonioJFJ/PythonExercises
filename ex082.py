# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_ímpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_ímpar.append(num)
    opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    while opção not in 'sn':
        opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    if opção in 's':
        continue
    elif opção in 'n':
        break
print()
print('Listas em ordem crescente')
print(f'\033[33mLista: {sorted(lista)}')
print(f'Lista dos valores pares: {sorted(lista_par)}')
print(f'Lista dos valores ímpares: {sorted(lista_ímpar)}\033[m')
