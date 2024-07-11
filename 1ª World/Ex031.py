''' Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preco da passagem, cobrando R$0,50 por km para viagens de ate 200km.
E R$0,45 para viagens mais longas.
'''

dist = float(input('Digite a distancia em km: '))
preco = dist*0.50 if dist <=200 else dist*0.45
print(f'Esse e o preco a pagar: {preco} R$')
# if dist < 200:
#     preco = dist*0.50
#     print(f'Vai pagar: {preco}R$')
# else:
#     preco = dist*0.45
#     print(f'Vai pagar: {preco}R$')