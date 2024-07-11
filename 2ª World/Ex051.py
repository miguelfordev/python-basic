# Ex051: Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

n = int(input('Digite um termo: '))
r = int(input('Digite a razao: '))
d = n + (10-1)*r
for c in range(n,d+r,r):
    print(c)
    
