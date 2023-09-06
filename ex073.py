# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Flamengo.

clubes = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza',
          'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
          'Vasco', 'América-MG', 'Coritiba')

print(f'\nOs 5 primeiros times do Brasileirão são: {clubes[0:5]}')
print(f'\nOs últimos 4 colocados são: {clubes[-4:]}')
print(f'\nA listagem em ordem alfabética é: {sorted(clubes)}')
if 'Flamengo' in clubes:
    print('\nO Flamengo está na posição', clubes.index('Flamengo')+1)
else:
    print(f'\nO Flamengo não está na lista.')
