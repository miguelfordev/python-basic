# Ex074: Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tuplaInteiro = ()
gerador = maior = menor = 0
for c in range(5):
    gerador = randint(0,100)
    tuplaInteiro += (gerador,)
    if c == 0:
        maior = gerador
        menor = gerador
    else:
        if gerador > maior:
            maior = gerador
        if gerador < menor:
            menor = gerador
print(f'A Tupla: {tuplaInteiro}. O maior numero: {maior} e o menor numero: {menor}.')

# Resolução do Professor: 

from random import randint 
numeros = ( randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10) )
print(f'Os valores sorteados foram:', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'/nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')