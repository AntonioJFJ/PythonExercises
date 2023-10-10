# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que seja monetários.

from utilidadesCeV import dado
from utilidadesCeV import moeda
p = dado.leiaDinheiro('preço')
a = dado.leiaAumento('porcentagem do aumento')
r = dado.leiaRedução('porcentagem da redução')
moeda.resumo(p, a, r)
