# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

jogador = {}
lista = []
partidas = []

while True:
    partidas.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    total = int(input(f'Nº de partidas de {jogador["Nome"]}: '))
    if total != 0:
        for gols in range(1, total+1):
            partidas.append(int(input(f'Qtd. gols na {gols}ª partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(jogador['Gols'])
    lista.append(jogador.copy())
    pergunta = str(input(' -> \033[7mQuer continuar [S/N]?\033[m ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input(' -> \033[7mQuer continuar [S/N]?\033[m ')).lower().strip()[0]
    if pergunta in 's':
        continue
    elif pergunta in 'n':
        break

print('-='*30)
print('\033[35mNº \033[m', end='')
for cabeçalho in jogador.keys():
    print(f'\033[35m{cabeçalho:<15}\033[m', end='')
print()
print('-'*50)
for k, v in enumerate(lista):
    print(f'\033[35m{k:>2} \033[m', end='')
    for d in v.values():
        print(f'\033[35m{str(d):<15}\033[m', end='')
    print()
print('-='*30)

opção = int(input('Digite o Nº para ver os dados do jogador (999 para sair): '))
while opção != 999:
    if 0 <= opção <= len(lista)-1:
        print(f' -> \033[7mDados do jogador {lista[opção]["Nome"]}\033[m')
        for j, g in enumerate(lista[opção]["Gols"]):
            print(f'Na partida {j+1} fez {g} gol(s).')
    else:
        print('\033[31mOpção inválida. Verifique o Nº e tente novamente.\033[m')
    opção = int(input('Digite o Nº para ver os dados do jogador (999 para sair): '))

print()
print('\033[7:33m<<Obrigado>>\033[m')



'''
1)
print(f'\033[35m{"Nº":<5}{"Nome":^10}{"Gols":^15}{"Total":>5}\033[m')
print('-'*40)
for índice in range(len(lista)):
    print(f'\033[35m{índice}     {lista[índice]["Nome"]}     {lista[índice]["Gols"]}     {lista[índice]["Total de gols"]}\033[m')
    
2)
for i in range(len(lista[opção]["Gols"])):
    print(f'Na partida {i+1} fez {lista[opção]["Gols"][i]} gol(s).')
'''
