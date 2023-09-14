# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_geral = [[], []]

for c in range(1, 8):
    num = (int(input(f'Digite o {c}º valor: ')))
    if num % 2 == 0:
        lista_geral[0].append(num)
    else:
        lista_geral[1].append(num)

print()
print(f'\033[33mLista Geral: {lista_geral}\033[m')
print(f'\033[34mLista Par: {sorted(lista_geral[0])}\033[m')
print(f'\033[35mLista Ímpar: {sorted(lista_geral[1])}\033[m')
