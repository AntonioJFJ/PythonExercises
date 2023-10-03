# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

import datetime


def voto(condição):
    idade = datetime.date.today().year - ano
    if 0 <= idade < 16:
        return f'\033[32mPara a idade de {idade} anos NÃO é possível votar.\033[m'
    elif 16 <= idade < 18 or 70 < idade <= 120:
        return f'\033[33mPara a idade de {idade} anos o voto é OPCIONAL.\033[m'
    elif 18 <= idade <= 70:
        return f'\033[31mPara a idade de {idade} anos o voto é OBRIGATÓRIO.\033[m'
    else:
        return f'\033[1:35mErro. Verifique o ano inserido e tente novamente.\033[m'


# Programa principal
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
