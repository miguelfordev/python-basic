# Ex086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta.
lista = [[],[],[]]
for c in range(3):
    for co in range(3):
        lista[c].append(int(input(f'Digite um valor para a posição [{c},{co}]: ')))
print('-='*25)
for c in range(3):
    for co in range(3):
        print(f'[ {lista[c][co]} ]',end='')
    print()

# Resolução do Professor:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()