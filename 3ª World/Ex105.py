# Ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas. - A maior nota - A menor nota - A média da turma - A situação (opcional). Adicione também as docstrings da função.

def notas(*notas, sit=False):
    todas_notas = {}
    todas_notas['total'] = len(notas)
    todas_notas['maior'] = max(notas)
    todas_notas['menor'] = min(notas)
    todas_notas['media'] = sum(notas)/len(notas)
    if sit == True:
        if todas_notas['media'] > 7:
            todas_notas['situacao'] = 'BOA'
        elif 7 > todas_notas['media'] >= 6:
            todas_notas['situacao'] = 'RAZÓAVEL'
        else:
            todas_notas['situacao'] = 'RUIM' 
    return todas_notas


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)

# Resolução do Professor:
def nnotas(*n, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
