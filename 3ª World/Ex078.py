'''             Listas - Parte 1 - Variaveis Compostas
------------------------------------------------------------------------------------

lanche = ['hamburguer','suco','pizza','picole']

------ INSERINDO NA LISTA ---------
lanche.append('pudim') -> ADICIONA O PUDIM AO FINAL DA LISTA
lanche.insert(0,'Hotdog') -> ADICIONA O HOTDOG NA POSIÇÃO 0

----- APAGANDO DA LISTA --------
del lanche[3] -> APAGA A PIZZA
lanche.pop(3) -> APAGA A PIZZA/NORMALMENTE ELIMINA O ULTIMO ELEMENTO
lanche.remove('pizza') -> VOCê INDICA O VALOR QUE VOCÊ QUER ELIMINAR

---- CRIAÇÃO DE LISTA PELO RANGE -----
valores = list[range(4,11)]

---- ORDENAÇÃO DE VALORES NA LISTA ----
valores = [8,2,5,4,9,3,0]
valores.sort() -> ORDENA OS VALORES EM ORDEM CRESCENTE
valores.sort(reverse=True) -> ORDENA OS VALORES EM ORDEM DECRESCENTE

---- TAMANHO DA LISTA ----
len(valores) -> RETORNA O TAMANHO DA LISTA/ELEMENTOS

---- BUSCANDO NA LISTA -----
valores.index(5) -> PRIMEIRA OCORRENCIA DO NUMERO 5

----- LIGAÇÃO DE LISTAS -----
a = [2,3,4,7]
b = a <- ISSO CRIA UMA LIGAÇÃO ENTRE AS LISTAS E TODA ALTERAÇÃO NA LISTA B ALTERA LISTA A.
b = a[:] <- CRIANDO UMA COPIA DA LISTA A
b[2] = 8 <- ALTERANDO SÓ O ELEMENTO 2 DA LISTA B
'''

# Ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

v = []
maior = menor = 0
for c in range(5):
    v.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        maior = v[c]
        menor = v[c]
    if v[c] > maior:
        maior = v[c]
    if v[c] < menor:
        menor = v[c]
print(f'A lista: {v}. Numero maior e sua posição: {maior} - {v.index(maior)+1}ª posição. Numero menor e sua posição: {menor} - {v.index(menor)+1}ª posição.')

# Resolução do Professor: 

listanum = []
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}ª: ')))
    if c == 0:
        mai = men = listanum[c]
    else: 
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Voce digitou os valores: {listanum}')
print(f'O maior valor foi: {mai} nas posições:',end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f'{i}...',end='')
print(f'O menor valor foi: {men} nas posições:')
for i,v in enumerate(listanum):
    if v == men:
        print(f'{i}...',end='')