# Ex100: Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
numeros = []
def sorteia():
    for x in range (5):
        numeros.append(randint(0,10))

def somaPar(x:list):
    soma = 0
    for _ in x:
        if _%2==0:
            soma += _
    return soma
sorteia()
numeros.sort()
print(f'A lista de numeros sorteados: {numeros}')
print(f'A soma dos numeros pares: {somaPar(numeros)}')

# Resolução do Professor:
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='',flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)
