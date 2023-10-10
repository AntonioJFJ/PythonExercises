# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
num = float(input('Digite um valor: R$ '))
while True:
    taxa = str(input('Digite a porcentagem da taxa: '))
    if taxa.isnumeric():
        taxa = float(taxa)
        break
print('-'*40)
print(f'\033[33mAumentando {taxa}% temos R$ {moeda.aumentar(num, taxa)}')
print(f'Diminuindo {taxa}% temos R$ {moeda.diminuir(num, taxa)}')
print(f'O dobro de R$ {num} é R$ {moeda.dobro(num)}')
print(f'A metade de R$ {num} é R$ {moeda.metade(num)}\033[m')
