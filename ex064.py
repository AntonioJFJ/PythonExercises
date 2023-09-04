# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


soma = 0
cont = 0
num = int(input('Digite um número inteiro \033[33m(OBS: Para parar digite 999)\033[m: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número inteiro \033[33m(OBS: Para parar digite 999)\033[m: '))

print('\n\033[32m{} números digitados e soma desses números igual a {}.\033[m'.format(cont, soma))
