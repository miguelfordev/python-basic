# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.

preco = float(input('\n Digite o preco do produto para aderir o seu desconto: '))
print('='*100)
print(f'O novo preco do produto e: {preco-(preco*5)/100} reais(R$).\n')