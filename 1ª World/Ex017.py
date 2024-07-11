#Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
cato = float(input('\nDigite o comprimento do cateto oposto: '))
cata = float(input('\nDigite o comprimento do cateto adjacente: '))

print(f'A hipotenusa e: {math.hypot(cato,cata):.2f}')