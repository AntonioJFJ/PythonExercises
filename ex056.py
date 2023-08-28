# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
homem_velho = 0
nome_velho = 0
cont_mulheres = 0


for c in range(1, 5):
    print('{}ª pessoa: '.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).lower()
    print('-'*40)
    soma_idade = soma_idade + idade
    if sexo == 'masculino':
        for man in range(1, 5):
            if c == 1 and sexo == 'masculino':
                homem_velho = idade
                nome_velho = nome
            else:
                if idade > homem_velho:
                    homem_velho = idade
                    nome_velho = nome
    if sexo == 'feminino' and idade < 20:
        cont_mulheres += 1

média = int(soma_idade/4)
print('\033[33mA média de idade do grupo é de {} anos.\033[m'.format(média))
print('\033[33mHomem mais velho tem {} anos e se chama {}.\033[m'.format(homem_velho, nome_velho))
print('\033[33m{} mulher(es) tem menos de 20 anos.\033[m'.format(cont_mulheres))

