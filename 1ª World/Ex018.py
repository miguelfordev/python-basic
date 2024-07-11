#Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
ang = float(input('\nDigite um angulo pra saber o seno, cosseno e tangente: '))
print(f'O seno e : {math.sin(math.radians(ang)):.2f}, o cosseno: {math.cos(math.radians(ang)):.2f} e a tangente: {math.tan(math.radians(ang)):.2f}\n')