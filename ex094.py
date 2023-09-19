# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
lista = []
mulheres = []
acima_média = []
tot_idade = 0
cont = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).lower().strip()[0]
    while dados['sexo'] not in 'mf':
        dados['sexo'] = str(input('Sexo [M/F]: ')).lower().strip()[0]
    if dados['sexo'] == 'f':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    cont += 1
    tot_idade += dados['idade']
    pergunta = str(input(' -> \033[7mQuer continuar [S/N]?\033[m ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input(' -> \033[7mQuer continuar [S/N]?\033[m ')).lower().strip()[0]
    if pergunta in 's':
        continue
    elif pergunta in 'n':
        break
média = int(tot_idade/cont)
if cont > 1:
    print(f'\033[35m{cont} pessoas foram cadastradas.')
else:
    print(f'{cont} pessoa foi cadastrada.')
print(f'A média de idade é de {média} anos.')
print(f'Mulheres: {mulheres}')
print('Pessoas com idade acima da média: ', end=' ')
for velho in lista:
    if velho['idade'] >= média:
        for k, v in velho.items():
            print(f'{k} = {v}; ', end=' ')
