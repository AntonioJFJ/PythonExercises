# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.date.today().year - ano
pessoa['CTPS'] = int(input('CTPS (digite 0, caso não tenha): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] + 35) - ano
    print('\033[33mDados\033[m'.center(40))
    print(f'Nome: {pessoa["Nome"]}')
    print(f'Idade: {pessoa["Idade"]} anos')
    print(f'CTPS: {pessoa["CTPS"]}')
    print(f'Ano de contratação: {pessoa["Ano de contratação"]}')
    print(f'Salário: R$ {pessoa["Salário"]:.2f}')
    print(f'Aposentadoria: {pessoa["Aposentadoria"]} anos')
    print('-' * 40)
else:
    print('\033[33mDados\033[m'.center(40))
    print(f'Nome: {pessoa["Nome"]}')
    print(f'Idade: {pessoa["Idade"]} anos')
    print('CTPS: N/A')
    print('-' * 40)
print('Obrigado. Volte sempre.')


'''for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')'''
