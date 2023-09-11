# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
expressão = str(input('Digite a expressão: '))
for símbolo in expressão:
    if símbolo == '(':
        lista.append('(')
    elif símbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[32mA expressão é válida.\033[m')
else:
    print('\033[31mA expressão é inválida.\033[m')
