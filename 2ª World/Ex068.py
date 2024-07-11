# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
cv = 0
while True:
    pc = randint(0,10)
    n = int(input("Digite um numero: "))
    while True:
        escolha = str(input("Digite se quer par ou impar: ")).lower().strip()
        if escolha == "par" or escolha == "impar":
            break
        else:
            print("COMANDO INVALIDO!") 
    if (n+pc)%2==0 and escolha == "par":
        print(f"Numero par: {n+pc} e você venceu!")
        cv += 1
    elif (n+pc)%2==1 and escolha == "impar":
        print(f"Numero impar: {n+pc} e você venceu!")
        cv += 1
    else:
        if (n+pc)%2==0 and escolha == "impar":
            print(f"Numero par: {n+pc} e você perdeu!")
            break
        elif (n+pc)%2==1 and escolha == "par":
            print(f"Numero impar: {n+pc} e você perdeu!")
            break
print("-"*50)
print(f"Voce teve: {cv} vitoria(s) consecutiva(s) no final do jogo! ")