# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.



num = int(input('Digite um número para visualizar sua tabuada: '))
print('\033[33mTabuada do {}\033[m'.format(num))
for c in range(1, 11):
    resultado = (c*num)
    print('{} x {:^2} = {}'.format(num, c, resultado))
print('FIM')


#number = 1
#print('{:02d}'.format(number))
#number == 01
