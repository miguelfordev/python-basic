# Ex082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas. 

lista=[]
par=[]
impar=[]
cont=0
while True:
    lista.append(int(input('Digite um valor: ')))
    if lista[cont]%2==0:
        par.append(lista[cont])
    else:
        if lista[cont]%2==1:
            impar.append(lista[cont])
    cont+=1
    r = input('Continue [S/N]: ').lower().strip()
    if r == 'n':
        break
par.sort()
impar.sort()
lista.sort()
print(f'Lista completa: {lista}')
print(f'Lista par: {par}')
print(f'Lista impar: {impar}')

# Resolução do Professor:
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v%2==0:
        pares.append(v)
    elif v%2==1:
        impares.append(v)
print(f'A lista completa e: {num}')
print(f'A lista de pares e: {pares}')
print(f'A lista de impares e: {impares}')