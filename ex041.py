# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Digite o ano de nascimento (yyyy): '))
idade = date.today().year - ano
if 0 <= idade <= 9:
    print('Sua idade é {} ano(s) e sua categoria é MIRIM.'.format(idade))
elif 10 <= idade <= 14:
    print('Sua idade é {} ano(s) e sua categoria é INFANTIL.'.format(idade))
elif 15 <= idade <= 19:
    print('Sua idade é {} ano(s) e sua categoria é JÚNIOR.'.format(idade))
elif 20 <= idade <= 25:
    print('Sua idade é {} ano(s) e sua categoria é SÊNIOR.'.format(idade))
elif 25 < idade <= 110:
    print('Sua idade é {} ano(s) e sua categoria é MASTER.'.format(idade))
else:
    print('Calma lá campeão!\nOu você nem nasceu ainda ou colocou a data errada.')
