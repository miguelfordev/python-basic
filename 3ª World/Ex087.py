# Ex087: Aprimore o desafio anterior, mostrando no final: a) A soma de todos os valores pares digitados. b) A soma dos valores da terceira coluna. c) O maior valor da segunda linha.
lista = [[],[],[]]
pares = v3 = maior = 0
for c in range(3):
    for c0 in range(3):
        lista[c].append(int(input(f'Digite um valor para a posição [{c},{c0}]: ')))
print('-='*25)
for c in range(3):
    for c0 in range(3):
        print(f'[ {lista[c][c0]} ]',end='')
        if lista[c][c0]%2==0:
            pares += lista[c][c0]
        if c0 == 2:
            v3 += lista[c][c0]
        if lista[1][c0] >= maior:
            maior = lista[1][c0]
    print()
print(f'A soma dos valores pares digitados: {pares}')
print(f'A soma dos valores da terceira coluna: {v3}')
print(f'Maior valor da segunda linha: {maior}')

# Resolução do Professor:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2==0:
            spar+=matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')