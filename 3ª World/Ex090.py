'''             Variáveis Compostas - Dicionários
-------------------------------------------------------------
dados = dict() ou dados = {}
dados = {"nome":"Pedro","idade":25}
print(dados["nome"]) --> Pedro
-------------------------------------------------------------
-- Adicionando elemento -- 
dados["sexo"] = "M"
-- Removendo elemento -- 
del dados["idade"]
-------------------------------------------------------------
Ex: filme = {"titulo":"Star Wars", "ano":1977, "diretor":"George Lucas"}
-- Diferenciando valores(values), item(items) e chaves(keys) --
print(filme.values()) --> "Star Wars",1977,"George Lucas"
print(filme.keys()) --> "titulo","ano","diretor"
print(filme.items()) --> "titulo":"Star Wars", "ano":1977, "diretor":"George Lucas"
------------------------------------------------------------
-- Copiando um dicionario para uma lista --
estado = {}
brasil = []
for c in range(0,3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
'''

# Ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
lista_alunos = []
while True:
    aluno["nome"] = str(input('Nome: '))
    aluno["média"] = float(input('Média: '))
    if aluno["média"] >= 6.5:
        aluno["situação"] = "APROVADO!"
    else:
        aluno["situação"] = "REPROVADO!"
    lista_alunos.append(aluno.copy())
    r = str(input('Continue?'))
    if r in 'nN':
        break
for aluno in lista_alunos:
    print(f"O aluno {aluno['nome']} teve média {aluno['média']} e seu status é: {aluno['situação']}.")

# Resolução do Professor:

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f'- {k} é igual a {v}')