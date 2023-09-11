# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Ordem crescente:
lista = []
for c in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1
print(f'\n{lista}')


# Ordem decrescente:
'''for c in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if c == 0 or num < lista[-1]:
        lista.append(num)
        print('Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num >= lista[pos]:
                lista.insert(pos, num)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1
print(f'\n{lista}')'''
