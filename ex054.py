# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

import datetime
cont = 0
Ncont = 0
Econt = 0
data_atual = datetime.date.today().year

for c in range(1, 8):
    print('{}ª pessoa'.format(c))
    ano = int(input('Digite seu ano de nascimento: '))
    idade = data_atual-ano
    print('-'*60)
    if 0 <= idade < 21:
        cont += 1
    elif idade >= 21:
        Ncont += 1

print('\033[31m{} pessoas ainda NÃO atingiram a maioridade.\033[m\n'
      '\033[32m{} pessoas JÁ atingiram a maioridade.\033[m'.format(cont, Ncont))

