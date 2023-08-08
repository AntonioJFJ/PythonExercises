# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ângulo = float(input('Informe o valor do ângulo (graus): '))
ânguloAjustado = math.radians(ângulo)
seno = math.sin(ânguloAjustado)
cosseno = math.cos(ânguloAjustado)
tangente = math.tan(ânguloAjustado)
print('Para o ângulo de {}º, temos:\nseno = {:.4f}\ncosseno = {:.4f}\ntangente = {:.4f}'
      .format(ângulo, seno, cosseno, tangente))
