# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if (reta1+reta2) > reta3 and (reta1+reta3) > reta2 and (reta2+reta3) > reta1:
    print('As 3 retas \033[32mPODEM\033[m formar um triângulo.')
else:
    print('As 3 retas \033[31mNÃO\033[m podem formar um triângulo.')
    exit()
if reta1 == reta2 == reta3:
    print('Este é um triângulo \033[42mEQUILÁTERO\033[m.')
elif reta1 != reta2 != reta3 != reta1:
    print('Este é um triângulo \033[42mESCALENO\033[m.')
else:
    print('Este é um triângulo \033[42mISÓSCELES\033[m.')

