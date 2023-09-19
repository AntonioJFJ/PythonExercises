# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome: '))
total = int(input('Nº de partidas: '))
score = 0
if total != 0:
    for gols in range(1, total+1):
        partidas.append(int(input(f'Qtd. gols na {gols}ª partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total de gols'] = sum(jogador['Gols'])
print('-='*40)
for k, v in jogador.items():
    print(f'\033[35m{k}: {v}\033[m')
print('-='*40)
print(f'\033[35m{jogador}\033[m')
print('-='*40)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f' -> Na partida {i+1} fez {v} gol(s).')
print(f'Foi um total de {jogador["Total de gols"]} gol(s).')
