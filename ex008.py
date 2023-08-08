# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite o valor da medida (m): '))
print('Metros: {} m\nCentímetros: {} cm\nMilímetros: {} mm'.format(medida, medida*100, medida*1000))
