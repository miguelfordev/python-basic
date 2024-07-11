# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci. Ex:0,1,1,2,3,5,8

n = int(input('Quanto elementos da sequencia de Fibonnaci deseja ver: '))
c = 3
e1 = 0
e2 = 1
if n == 1:
    print(f'{e1}\n')
if n == 2 or n >= 3:
    print(f'{e1}\n{e2}')
    if n >= 3:
        while c <= n:
            e3 = e1 + e2
            print(e3)
            e1 = e2
            e2 = e3
            c += 1