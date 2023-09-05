# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('='*40)
print('Tabuada'.center(40))
print('='*40)

while True:
    cont = 1
    print(cont)
    num = int(input('Coloque um número para ver sua tabuada: '))
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont:^2} = {num*cont}')
        cont = cont + 1

print('='*40)
