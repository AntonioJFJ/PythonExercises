# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time
import operator
resultados = {}
for jogadores in range(1, 5):
    resultados[f'Jogador {jogadores}'] = random.randint(1, 6)
ranking = dict()
print('\033[33mResultados dos dados\033[m'.center(40))
for k, v in resultados.items():
    time.sleep(1)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(resultados.items(), key=operator.itemgetter(1), reverse=True)
print('\033[33mOrdem de jogada\033[m'.center(40))
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
