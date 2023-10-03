# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome='DESCONHECIDO', gols=0):
    """
    -> Mostra o nome do jogador e quantos gols fez.
    :param nome: Nome do jogador.
    :param gols: Quantidade de gols.
    :return: retorna os dados do jogador.
    """
    if len(nome) < 1:
        nome = 'DESCONHECIDO'
    print('-' * 40)
    return f'\033[33mO jogador {nome} fez {gols} gol(s).\033[33m'


n = str(input('Nome do jogador: ')).upper().strip()
g = str(input('Qtd. de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(ficha(n, g))
