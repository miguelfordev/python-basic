'''         Importando/import
-----------------------------------------------------------------------
ex: Importando tudo da biblioteca: math
import math
num = int(input('Digite um numero: '))
print(f'A raiz quadrada desse numero e: {math.sqrt(num)}')

-----------------------------------------------------------------------
ex: importando especifico na biblioteca:
from math import sqrt,ceil
num = int(input('Digite um numero: '))
print(f'A raiz quadrada desse numero e: {ceil(sqrt(num))}')
-----------------------------------------------------------------------

ex: importando da biblioteca numero randomico
import random
num = random.randint(1,10)
print(num)
'''

#Ex016: Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteiro
import math
num = float(input('\nDigite um numero real: '))
print(f'A sua parte inteira e: {math.trunc(num)}')
print(f'A sua parte inteiro e: {int(num)}') #sem precisar importar modulo



