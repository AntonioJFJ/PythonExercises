# Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

import time
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
novo_n1 = 0
novo_n2 = 0
opções = ''


while opções != 5:
    opções = int(input(
        '\n\033[4mEscolha abaixo qual operação será realizada:\033[m\n\033[35m[1] somar\n[2] multiplicar\n[3] maior\n'
        '[4] novos números\n[5] sair do programa\n\033[m'))
    if opções == 1:
        print('\033[36mA soma entre {} e {} é igual a {}.\033[m'.format(n1, n2, (n1+n2)))
    elif opções == 2:
        print('\033[36mA multiplicação entre {} e {} é igual a {}.\033[m'.format(n1, n2, (n1*n2)))
    elif opções == 3:
        if n1 > n2:
            print('\033[36mO maior número entre os dois é {}.\033[m'.format(n1))
        elif n1 < n2:
            print('\033[36mO maior número entre os dois é {}.\033[m'.format(n2))
        else:
            print('\033[36mOs dois números são iguais.\033[m')
    elif opções == 4:
        novo_n1 = float(input('Digite o primeiro valor: '))
        novo_n2 = float(input('Digite o segundo valor: '))
        if novo_n1 != n1:
            n1 = novo_n1
        else:
            n1 = n1
        if novo_n2 != n2:
            n2 = novo_n2
        else:
            n2 = n2
        print('\033[36mOs novos números são {} e {}.\033[m'.format(n1, n2))
    elif opções == 5:
        print('\033[33mOpção 5 selecionada.')
    else:
        print('Opção inválida.')


time.sleep(1)
print('Saindo do programa...\033[m')
