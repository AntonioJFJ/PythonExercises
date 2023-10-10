# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

import moeda
num = float(input('Digite um valor: R$ '))
while True:
    taxa = str(input('Digite a porcentagem da taxa: '))
    if taxa.isnumeric():
        taxa = float(taxa)
        break
print('-'*40)
print(f'\033[33mAumentando {taxa}% temos {moeda.moeda(moeda.aumentar(num, taxa))}')
print(f'Diminuindo {taxa}% temos {moeda.moeda(moeda.diminuir(num, taxa))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}\033[m')
