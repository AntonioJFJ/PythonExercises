# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0, 5):
    lista.append((int(input(f'Digite um número para a posição {c}: '))))
maior = max(lista)
menor = min(lista)
print('-'*40)
print(f'\n\033[33mVocê digitou os valores {lista}\033[m')
print(f'O maior valor foi {maior} nas posições: ', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}', end='-')
print('FIM')
print(f'O menor valor foi {menor} nas posições: ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}', end='-')
print('FIM')
print('-'*40)
