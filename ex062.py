# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo da P.A.: '))
razão = int(input('Digite a razão da P.A.: '))
termo = a1
cont = 1
mais = 10
total = 0


print('\n\033[33mPara a1 igual a {} e razão igual a {}, os 10 primeiros termos são:\033[m'.format(a1, razão))
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[34m {} \033[m'.format(termo), end='')
        termo = termo + razão
        cont = cont + 1
    mais = int(input('\n\nQuantos termos a mais você gostaria de ver?\n\033[33mOBS: Selecione 0 para parar.\033[m\n'))

print('{} termos foram mostrados.'.format(total))


