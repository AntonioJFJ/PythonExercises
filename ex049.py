# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.



num = int(input('Digite um número para visualizar sua tabuada: '))
print('\033[33mTabuada do {}\033[m'.format(num))
for c in range(1, 11):
    print(c*num, end=' ')
print()
print('FIM')

