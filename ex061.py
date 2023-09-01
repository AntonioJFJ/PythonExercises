# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# an = a1 + (n – 1)r  -> Fórmula do termo geral de uma PA

a1 = int(input('Informe o primeiro termo da P.A.: '))
razão = int(input('Informe a razão da P.A.: '))
n = 1

print('\n\033[33mPara a1 igual a {} e razão igual a {}, os 10 primeiros termos são:\n\033[m'.format(a1, razão))
while n <= 10:
    an = a1 + (n - 1) * razão
    print(' {} '.format(an), end='')
    n += 1

