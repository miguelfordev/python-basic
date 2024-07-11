# Ex049: Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.

n = int(input('Digite um numero inteiro: '))
for c in range(1,11):
    print(f'{n}x{c}={n*c}')