# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

import time
print('\033[32mBem-vindo ao Bazar do Hardware 🖥\033[m'.center(60))
time.sleep(1)
print('-'*60)
nome = str(input('Qual é o seu nome?\n'))
produto = float(input('Informe o valor do produto: R$ '))
forma_de_pagamento = int(input('Qual a forma de pagamento?\n[1] Dinheiro\n[2] Cheque\n[3] Cartão\n'))
if forma_de_pagamento == 1:
    print('No dinheiro o produto tem 10% de desconto e sai a R$ {:.2f}.'.format(produto*0.9))
elif forma_de_pagamento == 2:
    print('No cheque o produto tem 10% de desconto e sai a R$ {:.2f}.'.format(produto*0.9))
elif forma_de_pagamento == 3:
    print('Pagamento no cartão escolhido.')
    vezes = int(input('Escolha a quantidade de parcelas:\n[1] à vista no cartão\n[2] 2x no cartão\n[3] 3x ou mais no cartão\n'))
    if vezes == 1:
        print('À vista no cartão o produto tem 5% de desconto e sai a R$ {:.2f}.'.format(produto*0.95))
    elif vezes == 2:
        print('Em 2x no cartão o produto NÃO tem desconto e sai a R$ {:.2f}.\n'
          'Parcelas no valor de R$ {:.2f}'.format(produto, produto/2))
    elif vezes == 3:
        parcelas = int(input('Escolha a quantidade de parcelas:\nDe 3x até 12x\n'))
        if 3 <= parcelas <= 12:
            print('Em {}x no cartão o produto tem 20% de juros e sai a R$ {:.2f}.\n'
                  'Parcelas no valor de R$ {:.2f}'.format(parcelas, produto * 1.2, (produto * 1.2) / parcelas))
        else:
            print('Erro. Preste atenção na quantidade de vezes informada.')
    else:
        print('Erro. Preste atenção nas opções disponíveis.')
else:
    print('Erro. Preste atenção nas opções disponíveis.')
print('Volte sempre, {} 🤝'.format(nome))
