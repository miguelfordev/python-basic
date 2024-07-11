'''             Aula 18 - Listas (Parte 2)
----------------------------------------------------------------
dados = ['Pedro',25]
            0     1

pessoas = list()
pessoas.append(dados[:]) <- ADICIONANDO NA LISTA PESSOAS UMA COPIA [:] DE DADOS
pessoas = [['Pedro',25],['Maria',19]] <- LISTA DENTRO DA LISTA
                0              1
print(pessoa[0][0]) <- 'Pedro'
'''     

# Ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas. b) Uma listagem com as pessoas mais pesadas. c) Uma listagem com as pessoas mais leves.

lista_pessoas = []
pessoas = []
lista_maior = []
lista_menor = []
maior = menor = 0
while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    pessoas.append(int(input('Digite o peso da pessoa: ')))
    if len(lista_pessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    lista_pessoas.append(pessoas[:])
    pessoas.clear()
    r = str(input('Continue?'))
    if r in 'Nn':
        break
for pessoas in lista_pessoas:
    if pessoas[1] == maior:
        lista_maior.append(pessoas[0])
    else:
        if pessoas[1] == menor:
            lista_menor.append(pessoas[0])
print(f'Quantidade de pessoas cadastradas: {len(lista_pessoas)}')
print(f'Maior peso foi: {maior}. E pessoas mais pesadas: {lista_maior}')
print(f'Menor peso foi: {menor}. E pessoas mais leves: {lista_menor}')

# Resolução do Professor:
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()