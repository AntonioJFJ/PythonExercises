# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo:\nM | F\n')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\033[31mResposta inválida.\033[m\n')

print('Obrigado.')
