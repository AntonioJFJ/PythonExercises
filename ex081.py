# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
contador = 0
while True:
    número = int(input('Digite um número: '))
    contador += 1
    if contador == 1 or número < lista[-1]:
        lista.append(número)
        print('Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if número >= lista[pos]:
                lista.insert(pos, número)
                print(f'Número adicionado na posição {pos}.')
                break
            pos += 1
    opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    while opção not in 'sn':
        opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    if opção in 's':
        continue
    elif opção in 'n':
        break

print(f'\n\033[33mForam digitados {contador} números.')
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado {lista.count(5)} vezes nas posições: ', end='')
    for p, v in enumerate(lista):
        if v == 5:
            print(f'{p}', end=' ')
else:
    print('O valor 5 não foi digitado.')
