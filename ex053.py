# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase sem caracteres especiais: ')).lower().strip().split()
junção = ''.join(frase)
invertido = junção[::-1]
if junção == invertido:
    print('\033[32mA frase é um palíndromo.\033[m')
    print('Frase original: {}'.format(junção))
    print('Frase invertida: {}'.format(invertido))
else:
    print('\033[31mA frase não é um palíndromo.\033[m')
    print('Frase original: {}'.format(junção))
    print('Frase invertida: {}'.format(invertido))



'''outra forma:
frase = str(input('Digite uma frase sem caracteres especiais: ')).lower().strip().split()
junção = ''.join(frase)
invertido = ''
for letra in range(len(junção)-1, -1, -1):
    invertido += junção[letra]
if invertido == junção:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')'''


