# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


valor = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
int(input('Digite um número: ')))
print(valor)
cont9 = valor.count(9)
cont3 = valor.count(3)

if cont9 >= 1:
    print(f'\033[33mO número 9 apareceu {cont9} vez(es).\033[m')
else:
    print(f'\033[33mO número 9 não estava presente na lista.\033[m')
if cont3 >= 1:
    print(f'\033[33mO primeiro 3 apareceu na {valor.index(3)+1}ª posição.\033[m')
else:
    print(f'\033[33mO número 3 não estava presente na lista.\033[m')

print(f'Os números pares foram: ', end='-')
for c in valor:
    if c%2 == 0:
        print(c, end='-')
