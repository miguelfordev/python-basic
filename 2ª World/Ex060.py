# Faca um programa que leia um numero qualquer e mostre seu fatorial. Ex:5!=5x4x3x2x1=120

n = int(input('Digite um numero para saber o fatorial: '))
fat = n*(n-1)
n = n-1
while True:
    fat *= (n-1)
    n = n-1
    if n == 1:
        break
print(f'fatorial de {n} e igual a: {fat}')

# Outros exemplos: 

from math import factorial

n1 = int(input("Digite o numero: "))
print(f"O fatorial de {n1} é igual a: {factorial(n1)}")