# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS: Considere que o caixa possui cedulas de 50, 20, 10 e 1.

valor = int(input("Qual será o valor sacado: "))
c50 = c20 = c10 = c1 = 0
tot = valor
while True: 
    if valor >= 50:
        while valor >= 50:
            valor -= 50
            c50 += 1
        print(f"Notas de R$50 sacadas: {c50}")
    if valor >= 20:
        while valor >= 20:
            valor -= 20
            c20 += 1
        print(f"Notas de R$20 sacadas: {c20}")
    if valor >= 10:
        while valor >= 10:
            valor -= 10
            c10 += 1
        print(f"Notas de R$10 sacadas: {c10}")
    if valor >= 1:
        while valor >= 1:
            valor -= 1
            c1 += 1
        print(f"Notas de R$1 sacadas: {c1}")
    if valor == 0:
        break

"""     Outro Exemplo:

print('-'*30)
print('{:^30}}'.format('BANCO CEV'))
print('-'*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
white True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('-'*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

"""