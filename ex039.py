# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se
# já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import time
from datetime import date
print('MINISTÉRIO DA DEFESA'.center(50))
print('-'*50)
time.sleep(1)
nome = str(input('Qual é o seu nome?\n'))
time.sleep(1)
print('Seja bem-vindo às Forças Armadas, \033[32m{}\033[m!'.format(nome))
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print('\033[32mIdade mínima para alistamento NÃO atingida!\nVocê deverá se apresentar em {} ano(s).'
          .format((ano+18) - date.today().year))

elif idade == 18:
    print('\033[1:33mApresente-se às Forças Armadas para apresentação e devido alistamento!')

else:
    reservista = int(input('Você é reservista/dispensado?\n[1]: Sim\n[2]: Não\n'))
if idade > 18 and reservista == 1:
    print('\033[32mObrigado por manter sua situação em dia com as Forças Armadas.')
elif idade > 18 and reservista == 2:
    print('\033[0:1:31mApresente-se imediatamente às Forças Armadas!\nVocê ULTRAPASSOU {} '
          'ano(s) do período de apresentação.'.format(date.today().year - (ano + 18)))

