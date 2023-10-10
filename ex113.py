# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            return '\033[31mO usuário saiu sem informar o número!\033[m'
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            return '\033[31mO usuário saiu sem informar o número!\033[m'
        else:
            return num


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print('-' * 50)
print(f'\033[33mO valor inteiro digitado foi {n1} e o real {n2}.\033[33m')
