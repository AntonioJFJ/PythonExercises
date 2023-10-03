# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, situação=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param notas: Notas dos alunos.
    :param situação: (opcional) Situação dos alunos.
    :return: dicionário com todas as informações.
    """
    print('-'*100)
    dados = {}
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['média'] = sum(notas)/len(notas)
    if situação:
        if 7 <= dados['média'] <= 10:
            dados['situação'] = 'Boa'
        elif 6 <= dados['média'] < 7:
            dados['situação'] = 'Razoável'
        else:
            dados['situação'] = 'Ruim'
    return f'\033[33m{dados}\033[m'


resp = notas(5.5, 2.5, 8.5, situação=True)
print(resp)
