#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere US$ 1.00 = R$ 3.27

din = float(input('\n Digite o valor em real(R$) que gostaria de converter: '))
print('='*100)
print(f'O valor em Real(R$):{din}, convertido e igual a Dolar(US$):{din/3.27:.2f}\n')