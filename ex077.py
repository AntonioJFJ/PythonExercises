# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

print('\033[36m=\033[m'*40)
print('VOGAIS'.center(40))
print('\033[36m=\033[m'*40)
palavras = ('CADEIRA', 'MESA', 'QUADRO', 'VENTILADOR', 'PORTA', 'JANELA')

for cont in palavras:
    print(f'\n{cont}:', end=' ')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(f'\033[33m{letra}\033[m', end=' ')
