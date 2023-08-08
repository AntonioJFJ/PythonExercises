# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O escolhido pelo professor foi {}'.format(sorteio))
