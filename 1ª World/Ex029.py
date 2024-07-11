''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7 por cada km acima do limite.
'''

vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel-80)*7
    print(f'Voce foi multado, vai pagar: {multa}R$')
else:
    print('nao foi multado')