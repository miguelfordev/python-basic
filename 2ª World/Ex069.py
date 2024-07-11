# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: a) Quantas pessoas tem mais de 18 anos. b) Quantos homens foram cadastrados. c) Quantas mulheres tem menos de 20 anos.
id18 = hm = m20 = 0
while True:
    idade = int(input("Digite a idade: "))
    while True:
        sexo = str(input("Digite o sexo [F/M]: ")).strip().upper()[0]
        if sexo == "F" or sexo == "M":
            break
        else:
            print("SEXO INVALIDO.")
    if idade >= 18:
        id18 += 1
    if sexo == "M":
        hm += 1
    if sexo == "F" and idade < 20:
        m20 += 1
    while True:
        resp = str(input("Voce quer continuar [S/N]: ")).strip().upper()
        if resp == "N" or resp == "S":
            break
        else:
            print("COMANDO INVALIDO")
    if resp == "N":
        break
print(f"Pessoas com mais de 18: {id18}, homens cadastrados: {hm} e mulheres com menos de 20: {m20}")