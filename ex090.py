# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

conteúdo = {}
conteúdo['Nome'] = str(input('Nome: '))
conteúdo['Média'] = float(input(f'Média de {conteúdo["Nome"]}: '))
print('-='*40)
if 7 <= conteúdo['Média'] <= 10:
    conteúdo['Situação'] = "\033[32mAprovado\033[m"
elif 5 <= conteúdo['Média'] < 7:
    conteúdo['Situação'] = "\033[33mRecuperação\033[m"
elif 0 <= conteúdo['Média'] < 5:
    conteúdo['Situação'] = "\033[31mReprovado\033[m"
else:
    conteúdo['Situação'] = "\033[1:35mErro. Verifique a média e tente novamente.\033[m"
for k, v in conteúdo.items():
    print(f'{k} é igual a {v}')
