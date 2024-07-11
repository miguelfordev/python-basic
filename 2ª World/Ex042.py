''' Desafio 42: Refaca o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

r = [int(input(f'Digite {x+1} reta: ')) for x in range(3)]
if r[0]<r[1]+r[2] and r[1]<r[0]+r[2] and r[2]<r[0]+r[1]:
    print('\33[0;35;45mpossivel fomar triangulo', end='')
    if r[0] == r[1] and r[1] == r[2]:
        print('Equilatero')
    elif r[0] == r[1] or r[1] == r[2] or r[0] == r[2]:
        print('isoceles')
    else:
        print('escaleno')
else:
   print('nao e possivel formar triangulo')