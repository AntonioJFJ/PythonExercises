# Adicione no módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda
while True:
    num = str(input('Digite um valor: R$ '))
    if num.isnumeric():
        num = float(num)
        break
while True:
    taxa_aumento = str(input('Digite a porcentagem do aumento: '))
    if taxa_aumento.isnumeric():
        taxa_aumento = float(taxa_aumento)
        break
while True:
    taxa_abatimento = str(input('Digite a porcentagem do abatimento: '))
    if taxa_abatimento.isnumeric():
        taxa_abatimento = float(taxa_abatimento)
        break
print('\033[1:33m~\033[m'*60)
moeda.resumo(num, taxa_aumento, taxa_abatimento)
