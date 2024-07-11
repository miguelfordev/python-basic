# Ex048: Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
soma=0
ct=0
for c in range (1,501,2):
    if c%3==0:
        soma += c
        ct += 1
print(f'A soma de todos os {ct} numeros sao: {soma}')