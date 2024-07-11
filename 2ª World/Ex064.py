# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
n = digi = soma = 0
n = int(input('Digite um numero: '))
while n != 999:
    soma += n
    n = int(input('Digite um numero: '))
    digi += 1
    

print(f"Voce digitou: {digi} numeros e a soma foi: {soma}") 