# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_geral = []
lista_aluno = []

print('\033[33mBoletim Escolar\033[m'.center(80))
print('-'*80)
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista_aluno.append(nome)
    lista_aluno.append(nota1)
    lista_aluno.append(nota2)
    lista_geral.append(lista_aluno[:])
    lista_aluno.clear()
    pergunta = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    if pergunta in 'n':
        break
    elif pergunta in 's':
        continue

print('-'*40)
print(f'\033[35m{"Nº":<5}{"Nome":^10}{"Média":>5}\033[m')
print('-'*40)
for índice in range(0, len(lista_geral)):
    print(f'\033[35m{índice:<5}{lista_geral[índice][0]:^10}{((lista_geral[índice][1])+(lista_geral[índice][2]))/2:>5}\033[m')

opção = int(input('Escolha o número do aluno para ver suas notas (999 para sair): '))
while opção != 999:
    if 0 <= opção <= len(lista_geral)-1:
        print(f'Notas de {lista_geral[opção][0]} são: {lista_geral[opção][1:]}')
        print('-' * 40)
    else:
        print('\033[31mOpção inválida. Verifique o Nº e tente novamente.\033[m')
    opção = int(input('Escolha o número do aluno para ver suas notas (999 para sair): '))
print('-'*80)
print('\033[33mBoletim Escolar\033[m'.center(80))
