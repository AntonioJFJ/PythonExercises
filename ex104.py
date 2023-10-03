# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(num):
    print('-'*40)
    num = input('Digite um número: ')
    while True:
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mErro. Digite um número inteiro!\033[m')
            num = input('Digite um número: ')
            continue
    return num


n = leiaInt('Digite um número: ')
print(f'\033[33mVocê digitou o número {n}.\033[33m')
