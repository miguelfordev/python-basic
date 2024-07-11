''' Desafio 41: A Confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Ate 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos: JUNIOR
- Ate 20 anos: SENIOR
- Acima: MASTER
'''
from datetime import date
ano = int(input('\nDigite o ano de nascimento: '))
atual = date.today().year
if atual-ano < 9:
    print('mirim')
elif atual-ano >= 9 and atual-ano < 14:
    print('infantil')
elif atual-ano >= 14 and atual-ano < 19:
    print('junior')
elif atual-ano >= 19 and atual-ano < 20:
    print('senior')
else:
    print('master')