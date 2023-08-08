# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

l = float(input('Digite a medida correspondente a largura da parede (m): '))
a = float(input('Digite a medida correspondente a altura da parede (m): '))
área = l*a
t = área/2
print('A área da parede é de {:.2f} m² e será necessário {:.1f} litro(s) de tinta para pintá-la.'.format(área, t))
