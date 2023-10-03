# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def consulta():
    import time
    while True:
        msg_inicial = '  SISTEMA DE AJUDA PyHelp  '
        print('\033[m\033[42m~'*len(msg_inicial))
        print(f'\033[1:42m{msg_inicial}')
        print('\033[42m~'*len(msg_inicial))
        opção = str(input('\033[mFunção ou Biblioteca > ')).lower()
        if opção in 'fim':
            msg_final = '  Fechando o programa  '
            print('\033[41m~' * len(msg_final))
            print(f'\033[1:41m{msg_final}')
            print('\033[41m~' * len(msg_final))
            time.sleep(2)
            break
        else:
            msg_loading = f'  Acessando o manual do comando \'{opção}\'  '
            print('\033[44m~' * len(msg_loading))
            print(f'\033[1:44m{msg_loading}')
            print('\033[44m~' * len(msg_loading))
            time.sleep(2)
            print('\033[7:40m')
            print(help(opção))


consulta()
