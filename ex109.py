# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda
num = float(input('Digite um valor: R$ '))
while True:
    taxa = str(input('Digite a porcentagem da taxa: '))
    if taxa.isnumeric():
        taxa = float(taxa)
        break
print('-'*40)
print(f'\033[33mAumentando {taxa}% temos {moeda.aumentar(num, taxa, True)}')
print(f'Diminuindo {taxa}% temos {moeda.diminuir(num, taxa, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}\033[m')
