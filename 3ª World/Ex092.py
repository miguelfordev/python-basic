# Ex092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
aposentados = {}
lista_aposentados = []
while True:
    aposentados['nome'] = str(input('Nome: '))
    aposentados['idade'] = int(date.today().year)-int(input('Ano de nascimento: '))
    aposentados['ctps'] = int(input('CTPS: '))
    if aposentados['ctps'] != 0:
        aposentados['anoC'] = int(input('Ano de contratação: '))
        aposentados['salario'] = float(input('Salario: '))
        anos_trabalhados = int(date.today().year) - aposentados['anoC']
        if anos_trabalhados < 35:
            aposentados['aposentadoria'] = aposentados["idade"]+(35 - anos_trabalhados)
    lista_aposentados.append(aposentados.copy())
    r = str(input('Continue?'))
    if r in 'nN':
        break
for aposentado in lista_aposentados:
    print(f'''Contribuinte: {aposentado["nome"]},
        Idade: {aposentado["idade"]} anos,
        CTPS: {aposentado["ctps"]},
        ''',end='')
    if aposentado["ctps"] != 0:
        print(f'''Ano de contratação: {aposentado["anoC"]},
        Salário no valor: {aposentado["salario"]},
        Aposentadoria: {aposentado["aposentadoria"]} anos
        ''')
    print()

# Resolução do Professor:
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+35)-datetime.now().year)
print('-='*30)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')