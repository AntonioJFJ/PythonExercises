# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if (num1-num2) >=0 and (num1-num3) >=0:
    print('O maior número é {}.'.format(num1))
elif (num2-num1) >=0 and (num2-num3) >=0:
    print('O maior número é {}.'.format(num2))
elif (num3-num1) >=0 and (num3-num2) >=0:
    print('O maior número é {}.'.format(num3))
if (num1-num2) <=0 and (num1-num3) <=0:
    print('O menor número é {}.'.format(num1))
elif (num2-num1) <=0 and (num2-num3) <=0:
    print('O menor número é {}.'.format(num2))
elif (num3-num1) <=0 and (num3-num2) <=0:
    print('O menor número é {}.'.format(num3))




'''Código mais compacto:
1)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
ordem = [num1, num2, num3]
ordem.sort()
print(f'O menor número é {ordem[0]} e o maior é {ordem[2]}')
--------------------------------------------------------------
2)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print('O menor número é {}'.format(menor))
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O maior número é {}'.format(maior))'''