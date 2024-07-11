# Ex052: Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

n = int(input('Digite um numero inteiro: '))
s =0
for c in range(1,n+1):
    if n%c==0:
        s +=1
if s == 2:
    print('primo')
else:
    print('nao e primo')    