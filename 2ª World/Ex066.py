"""         Aula 15 - Interrompendo Repetições while
--------------------------------------------------------------

Exemplo:
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
"""

# Ex066: Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
c = soma = 0
while True:
    n = int(input("Digite um numero inteiro: "))
    if n == 999:
        break
    soma += n
    c +=1
print(f"Numeros digitado: {c} e a soma deles: {soma}")