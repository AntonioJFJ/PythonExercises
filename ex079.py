# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

while True:
    valores = (int(input('Digite um número: ')))
    if valores not in lista:
        lista.append(valores)
    else:
        print('\033[31mValor duplicado. Não será adicionado.\033[m')
    opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    print('-' * 30)
    while opção not in 'sn':
        opção = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    if opção in 'n':
        break
    elif opção in 's':
        continue
    else:
        print('\033[31mOpção inválida.\033[m')
print('-'*30)
print(f'Você digitou: \033[33m{lista}\033[m')
print(f'Lista em ordem crescente: \033[34m{sorted(lista)}\033[m')
