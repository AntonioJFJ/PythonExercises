# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

URL = 'http://pudim.com.br'

try:
    response = requests.head(URL)
except Exception as erro:
    print('\033[41mO site não está funcionando!\033[m')
    print()
    print(f'\033[31mNão OK: {str(erro)}\033[m')
    print('\033[33mVerifique os seguintes passos:\n'
          '1) Se a internet está funcionando\n'
          '2) Se o site possui \'http://\' ou \'https://\' no início\n'
          '3) Se o restante do site foi digitado corretamente\033[m')
else:
    if response.status_code == 200:
        print('\033[42mO site está funcionando!\033[m')
    else:
        print(f'\033[31mNão OK: HTTP response code {response.status_code}\033[m')
