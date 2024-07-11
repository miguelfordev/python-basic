# Ex054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

from datetime import date
menor =0
maior =0
for c in range(7):
    nasc = int(input('Digite o ano de nascimento: '))
    atual = date.today().year
    if atual-nasc <= 17:
        menor += 1
    else:
        maior += 1
print(f'Pessoas menores de 18: {menor} e maiores de 18: {maior}')