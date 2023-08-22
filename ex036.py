# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

valor_casa = float(input('Informe o valor do imóvel: R$ '))
salário = float(input('Informe o salário do comprador: R$ '))
financiamento = int(input('Informe o período de financiamento (anos): '))
mensalidade = (valor_casa/(financiamento*12))
if mensalidade > (salário*0.3):
    print('\033[31mInfelizmente o empréstimo não poderá ser concedido nessas condições.\nA prestação mensal ultrapassa '
          '30% do seu rendimento em R$ {:.2f}.\033[m\n\033[33mPrestação mensal: R$ {:.2f}'
          .format((mensalidade-(salário*0.3)), mensalidade))
else:
    print('\033[32mParabéns! O empréstimo foi aprovado e em breve cairá em sua conta.\033[m'
          '\n\033[33mPrestação mensal: R$ {:.2f}'.format(mensalidade))
