# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time
print('\033[32m*\033[m'*60)
print('\033[33mPalpites Mega-Sena\033[m'.center(60))
print('\033[32m*\033[m'*60)
pergunta = int(input('Quantos jogos você vai fazer?\n'))
print('-'*40)
print(f'Sorteando {pergunta} jogos'.center(40))
print('-'*40)
lista_geral = []
lista_palpite = []

for jogos in range(1, pergunta+1):
    lista_palpite.clear()
    for números in range(0, 6):
        sorteio = random.randint(1, 60)
        if sorteio not in lista_palpite:
            lista_palpite.append(sorteio)
    lista_geral.append(sorted(lista_palpite[:]))
    time.sleep(1)
    print(f'Jogo {jogos}: {sorted(lista_palpite)}')
print('-'*40)
print(f'Lista geral: {lista_geral}')
