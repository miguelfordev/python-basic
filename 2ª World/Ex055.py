# Ex055: Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=0
for c in range(5):
    peso = float(input('Digite o peso: '))   
    if c ==0:
         maior=peso
         menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(menor,maior)
    