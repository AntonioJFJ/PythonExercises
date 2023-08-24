# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)
if 0 <= imc < 18.5:
    print('Seu IMC é {:.2f}\n\033[31mVocê está Abaixo do Peso\033[m.'.format(imc))
elif 18.5 <= imc <=25:
    print('Seu IMC é {:.2f}\n\033[32mVocê está no Peso Ideal\033[m.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}\n\033[33mVocê está com Sobrepeso\033[m.'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f}\n\033[31mVocê está com Obesidade\033[m.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}\n\033[31:41mVocê está com Obesidade Mórbida\033[m.'.format(imc))
elif imc < 0:
    print('\033[45mErro. Verifique o peso e a altura e tente novamente, pois seu IMC foi {:.2f}.\033[m'.format(imc))

