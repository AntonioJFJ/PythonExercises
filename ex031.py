# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

import time
print('Bem-vindo à Viação Guanabara! 🚌')
print('-'*40)
time.sleep(1)
distância = float(input('Digite a distância da viagem (km): '))
if 0<distância<=200:
    print('O preço da passagem é R$ {:.2f}'.format(distância*0.5))
elif distância<=0:
    print('Erro. Verifique a distância informada e tente novamente!')
elif distância>200:
    print('O preço da passagem é R$ {:.2f}'.format(distância*0.45))
print('-'*40)
time.sleep(1)
print('Obrigado por viajar conosco!')
