# Ex088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
lista = []
while True:
    vz = int(input('Quantos jogos sorteados --> '))
    for c in range(vz):
        lista.clear()
        while len(lista) != 6:
            aleatorio = randint(1,60)
            if aleatorio not in lista:
                lista.append(aleatorio)
            lista.sort()
        print(f'{c+1}º Jogo: {lista}')
    r = str(input('Quer mais jogos [S/N]? --> '))
    if r in 'nN':
        break

# Resolução do Professor:
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('     JOGA NA MEGA SENA       ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in  enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)