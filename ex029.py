# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro (km/h)?\n'))
valor_da_multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado por ultrapassar a velocidade de 80km/h da via.\nO valor da multa será de R$ {}.'.format(valor_da_multa))
elif 0<=velocidade<40:
    print('Cuidado! Velocidade muito baixa na via.')
elif velocidade < 0:
    print('Erro. Foi digitada uma velocidade menor que 0 km/h.')
else:
    print('Obrigado por respeitar os limites da via.')
