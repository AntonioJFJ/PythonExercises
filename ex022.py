#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
maiúsculo = nome.upper()
print('Seu nome em maiúsculo é: {}'.format(maiúsculo))
minúsculo = nome.lower()
print('Seu nome em minúsculo é: {}'.format(minúsculo))
espaço0 = nome.split()
junção = ''.join(espaço0)
caracteres = len(junção)
print('Seu nome tem ao todo {} letras'.format(caracteres))
nome1 = espaço0[0]
caracteres1 = len(nome1)
print('Seu primeiro nome é {} e tem {} letras'.format(nome1, caracteres1))
