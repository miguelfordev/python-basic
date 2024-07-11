# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos os valores e qual foi o maior, e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
cont = soma = maior = menor = 0
resp = "S"
while resp in "Ss" :
    n = int(input("Digite o termo: "))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Voce quer continuar a digitar valor: [S/N] ")).strip().upper()[0]   
media = soma/cont
print(f"Teve: {cont} numeros digitados. Maior valor foi: {maior} e o menor foi: {menor} e a media foi: {media:.2f}")