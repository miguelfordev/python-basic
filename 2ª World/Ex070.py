# Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: a) Qua é o total gasto na compra. b) Quantos produtos custam mais de RS1.000. c) Qual é o nome do produto mais barato. 
totG = totM = c = pr = 0
nB = ""
while True:
    nome = str(input("Digite o nome do produto: ")) 
    preco = float(input("Digite o preço do produto: "))
    totG += preco
    c += 1
    if preco > 1000:
        totM += 1
    if c == 1 or pr > preco:
        nB = nome
        pr = preco
    while True:
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()
        if resp == "S" or resp == "N":
            break
        else:
            print("COMANDO INVALIDO")
    if resp == "N":
        break
print(f"Total gastos: {totG}, produtos mais de 1000: {totM} e produto mais barato: {nB}")