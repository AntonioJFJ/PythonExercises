# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# an = a1 + (n – 1)r  -> Fórmula do termo geral de uma PA

termo = int(input('Informe o primeiro termo da P.A.: '))
razão = int(input('Informe a razão da P.A.: '))
termo_final = termo+(razão*9)+1

print('Para a1 igual a {} e razão igual a {}, os 10 primeiros termos são:'.format(termo, razão))
for c in range(termo, termo_final, razão):
    print(c, end=' - ')
print('FIM')
