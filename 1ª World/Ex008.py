#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('\n Digite o valor em metros: '))
print('='*100)
print(f'O valor convertido em centimetros e igual a {metros*100:.1f} cm',end=' ')
print(f'e em milimetros e igual a {metros*1000:.1f}mm\n')