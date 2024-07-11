'''Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um sod digitos separados.
ex: Digite um numero: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''
numero = int(input('\nDigite um numero entre 0 e 9999: '))
print(f'Unidade: {numero//1%10}, Dezena: {numero//10%10}, Centena: {numero//100%10} e Milhar: {numero//1000%10}')