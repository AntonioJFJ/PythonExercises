# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('\033[36m=\033[m'*60)
print('\033[1:33mLISTAGEM DE PREÇOS\033[m'.center(60))
print('\033[36m=\033[m'*60)

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 20.00, 'Transferidor', 10.00, 'Compasso', 10.00,
         'Mochila', 200.00, 'Caneta', 3.00, 'Livro', 40.00)

for c in range(0, len(itens), 2):
    print(f'{itens[c]:.<40}', end='')
    print(f'R$ {itens[c+1]:>6.2f}')

print('='*60)
