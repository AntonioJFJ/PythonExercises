# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo:\nM | F\n')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[31mResposta inválida.\033[m\nEscolha entre:\nM | F\n'))

print('Obrigado.')
