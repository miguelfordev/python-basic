# Refaca o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while.

n = int(input('Digite um termo: '))
r = int(input('Digite a razao: '))
d = n + (10-1)*r

# for c in range(n,d+r,r):
#     print(c)

print(n)
while n != d:
    n=n+r
    print(n)

