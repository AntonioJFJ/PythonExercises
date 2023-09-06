# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'\033[33mVocê digitou {extenso[num]}.\033[m')
        opção = str(input('Você quer continuar [S/N]? ')).lower().strip()[0]
        while opção not in 'sn':
            opção = str(input('Você quer continuar [S/N]? ')).lower().strip()[0]
        if opção in 'n':
            break
