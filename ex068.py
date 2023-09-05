# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
print('-'*60)
print('\033[33mJogo do Par ou Ímpar\033[m'.center(60))
print('-'*60)
cont = 0
while True:
    pc = random.randint(0, 10)
    usuário = int(input('Escolha um número de 0 a 10: '))
    escolha = str(input('Par ou Ímpar? ')).lower().strip()[0]
    calc = pc+usuário
    if 0 <= usuário <= 10:
        if escolha in 'p':
            if (calc%2) == 0:
                print('\033[32mVocê ganhou')
                print(f'Eu escolhi {pc} e você {usuário}. {pc+usuário} igual a PAR\033[m')
                cont = cont + 1
                print('-' * 60)
            elif (calc%2) != 0:
                print('\033[31mVocê perdeu')
                print(f'Eu escolhi {pc} e você {usuário}. {pc+usuário} igual a ÍMPAR\033[m')
                print('-' * 60)
                break
        elif escolha in 'i':
            if (calc%2) != 0:
                print('\033[32mVocê ganhou')
                print(f'Eu escolhi {pc} e você {usuário}. {pc+usuário} igual a ÍMPAR\033[m')
                cont = cont + 1
                print('-' * 60)
            elif (calc%2) == 0:
                print('\033[31mVocê perdeu')
                print(f'Eu escolhi {pc} e você {usuário}. {pc+usuário} igual a PAR\033[m')
                print('-' * 60)
                break
        else:
            print('\033[31mOpção inválida. Escolha Par ou Ímpar\033[m')
    else:
        print('\033[31mOpção inválida. Escolha entre 0 e 10.\033[m')

print(f'\033[33mVocê teve um total de {cont} vitória(s) consecutivas.\033[m')
