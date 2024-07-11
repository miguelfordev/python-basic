# Ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*lst):
    if len(lst) != 0:
        for x in lst:
            print(x,end=' ')
    print(f'Foram informado(s) {len(lst)} valor(es).')
    if len(lst) == 0:
        print('O maior valor informado foi 0/nulo/vazio.')
    if len(lst) > 0:
        print(f'O maior valor informado {max(lst)}.')
    print('-='*35)
    
maior(2,9,4,5,7,1)
maior(0,4,7)
maior(1,2)
maior(6)
maior()

# Resolução do Professor:
from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2,9,4,5,7,1)
maior(0,4,7)
maior(1,2)
maior(6)
maior()