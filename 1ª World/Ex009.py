# Faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('\n Digite um numero inteiro para saber a tabuada: '))
print('='*100)
c = 0
while (c < 11):
    print(f'{numero} x {c} = {numero*c}\n')
    c = c + 1