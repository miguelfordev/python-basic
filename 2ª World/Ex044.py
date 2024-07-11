''' Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
- A vista dinheiro/cheque:
    10% de desconto
- A vista no cartao:
    5% de desconto
- Em ate 2x no cartao:
    preco normal
- 3x ou mais no cartao:
    20% de juros
'''
print(f'='*20," LOJAS GUANABARA ", '='*20)
preco = float(input('\nDigite o valor do produto: '))
print(f'''FORMAS DE PAGAMENTO:
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO''')
pgt = str(input('Digite a fomra de pagamento: '))

if pgt == '1':
    print(f'Novo valor do produto {preco-(preco*10)/100}')
elif pgt == '2':
    print(f'Novo valor do produto {preco-(preco*5)/100}')
elif pgt == '3':
    print(f'Novo valor do produto {preco}, 2x de {preco/2}, sem juros')
elif pgt == '4':
    op = int(input('Quantas vezes quer parcelar: '))
    print(f'Novo valor do produto {preco+(preco*20)/100}, {op}x de {(preco+(preco*20)/100)/op:.2f}, com juros')
else:
    print('ALERTA! COMANDO INVALIDO.')