# Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input("De qual numero quer saber a tabuada: "))
    if n >= 0:
        for c in range(11):
            print(f"{c} x {n} = {c*n}")
    if n < 0:
        break