# Ex094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas. b) A média de idade do grupo. c) Uma lista com todas as mulheres. d) Uma lista com todas as pessoas com idade acima da média.
pessoa = {}
lista_pessoa = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).lower()
        if pessoa['sexo'] in 'mf':
            break
        print('Erro, digite somente M ou F')
    pessoa['idade'] = int(input('Idade: '))
    lista_pessoa.append(pessoa.copy())
    while True:
        r = str(input('Continue [S/N]? '))
        if r in 'nNsS':
            break
        print('Erro, digite apenas S ou N')
    if r in 'nN':
        break
print(f'- O grupo tem {len(lista_pessoa)} pessoas.')
soma = 0
for valor in lista_pessoa:
    soma += valor['idade'] 
print(f'- A média de idade é de: {soma/len(lista_pessoa)} anos.')
print('- Mulheres cadastradas: ',end='')
for mulheres in lista_pessoa:
    if mulheres['sexo'] == 'f':
        print(mulheres['nome'],end=' ')
print()
print(f'- Lista de pessoas acima da média: ')
for value in lista_pessoa:
    if value['idade'] > soma/len(lista_pessoa):
        print(f'Nome: {value["nome"]}, sexo: {value["sexo"]}, idade: {value["idade"]}')

# Resolução do Professor:
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastras foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
