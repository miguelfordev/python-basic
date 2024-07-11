'''15) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

km = float(input('\n Digite a quantidade de Km percorridos: '))
dias = int(input('Dias alugados: '))
print(f'O total a pagar e: {(dias*60)+(km*0.15)}')