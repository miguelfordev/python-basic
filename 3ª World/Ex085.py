# Ex085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
lista=[[],[]]
while True:
    var = int(input('Digite um numero: '))
    if var%2==0:
        lista[0].append(var)
    else:
        if var%2==1:
            lista[1].append(var)
    resp = str(input('Continue? [S/N]'))
    if resp in 'nN':
        break
lista[0].sort()
lista[1].sort()
print(lista)

# Resolução do Professor: 
núm = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor%2==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores impares digitados foram: {núm[1]}')