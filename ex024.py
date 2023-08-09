# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da cidade?\n')).strip().upper().split()
resultado = cidade[0] == 'SANTO'
print('A cidade começa com Santo?\n{}'.format(resultado))

#-1=='Não', 0=='Sim'
