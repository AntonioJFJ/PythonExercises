# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
pares = coluna3 = 0
linha2 = []
for l in range(0, 3):
        for c in range(0, 3):
                num = (int(input(f"Digite um valor para [{l},{c}]: ")))
                matriz[l].append(num)
                if num % 2 == 0:
                    pares += num
                if c == 2:
                    coluna3 += num
                if l == 1:
                    linha2.append(num)
print('-='*30)
for l in range(0, 3):
        for c in range(0, 3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print()
max_linha2 = max(linha2)
print(f'\033[33mA soma dos valores pares é {pares}.')
print(f'\033[33mA soma dos valores da 3ª coluna é {coluna3}.')
print(f'\033[33mO maior valor da 2ª linha é {max_linha2}.')
