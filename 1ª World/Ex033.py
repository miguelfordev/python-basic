''' Faca um programa que leia tres numeros e mostre qual e o amior e qual e o menor.
'''
n = [float(input(f'digite o {x+1} numeros: ')) for x in range(3)]
if n[0]>n[1] and n[0]>n[2]:
    print(n[0],' e o maior.')
elif n[1]>n[0] and n[1]>n[2]:
    print(n[1],' e o maior')
else:
    print(n[2],' e o maior')

if n[0]<n[1] and n[0]<n[2]:
    print(n[0],' e o menor.')
elif n[1]<n[0] and n[1]<n[2]:
    print(n[1],' e o menor')
else:
    print(n[2],' e o menor')