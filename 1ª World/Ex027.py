'''Faca um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o ultimo nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza
'''
nome_completo = input('\nDigite seu nome comleto: ').split()
#lista_nome_separado = nome_completo.split()
#print(f'Primeiro nome: {lista_nome_separado[0]}, ultimo nome: {lista_nome_separado[len(lista_nome_separado)-1]}')
print(f'Primeiro nome: {nome_completo[0]}, ultimo nome: {nome_completo[len(nome_completo)-1]}')
