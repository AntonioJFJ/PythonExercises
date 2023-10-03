# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def fatorial(valor, show=False):
    """
    -> Calcula o fatorial de um número.
    :param valor: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: o fatorial do número escolhido.
    """
    print('-'*60)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == 1:
            if c > 1:
                print(f'\033[33m{c} x ', end='')
            else:
                print(f'{c} = \033[m', end='')
    return f


num = int(input('Digite um número para ver o seu fatorial: '))
opção = str(input('Quer ver a conta do fatorial [S/N]? ')).lower().strip()[0]
while opção not in 'sn':
    opção = str(input('Quer ver a conta do fatorial [S/N]? ')).lower().strip()[0]
if opção in 's':
    opção = True
else:
    opção = False
print(f'\033[33m{fatorial((num), show=opção)}\033[m')
