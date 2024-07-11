'''Desafio 39: Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
- Se ja passou do tempo de alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
# Entrada de dados
ano = int(input('\nDigite o ano de nascimento: '))
anoAt = date.today().year
# Estrutura de controle - Condicional
if (anoAt-ano) < 18:
    print(f'Idade: {anoAt-ano} anos. Falta {18-(anoAt-ano)} anos')
elif (anoAt-ano) == 18:
    print(f'Idades  {anoAt-ano} anos. Esta na hora de se alistar')
elif (anoAt-ano) > 18:
    print(f'Idade: {anoAt-ano} anos. Ja passou {(anoAt-ano)-18} anos')
else:
    print('Comando invalido.')