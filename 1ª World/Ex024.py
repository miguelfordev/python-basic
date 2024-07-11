'''Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO".
'''
cidade = input('\nDigite o nome da cidade: ').strip().lower()
if 'santo' in cidade.lower() and 'santo' in cidade[0:5].lower():
    print(f'Tem nome Santo e comeca com santo')
elif 'santo' in cidade.lower():
    print(f'Tem nome Santo mas nao comeca com santo')
else:
    print('Nao tem nome Santo')