'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''
nome = input('\nDigite um nome: ')
if 'silva' in nome.lower():
    print('Ela tem silva')
else:
    print('Nao tem silva')