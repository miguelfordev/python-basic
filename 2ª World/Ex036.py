'''                         Curso de Python 3 - Mundo 2 - Curso em Video
----------------------------------------------------------------------------------------
    - ESTRUTURAS DE CONTROLE - CONDICIONAIS ANINHADAS.
        if
        elif
        else
    
---------------------------------------------------------------------------------------        
    ex:
        nome = str(input('Digite seu nome: ')).lower()
        if nome == 'gustavo'
            print('Que nome bonito')
        elif nome == 'pedro' or nome == 'maria':
            print('seu nome e bem popular')
        elif nome in 'ana claudia jessica juliana':
            print('belo nome feminino')
        else:
            print('seu nome e bem normal')
        print(f'Tenha um bom dia {nome}')
'''

'''Desafio 36: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo quie ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
'''
# Entrada de dados:
casa = float(input('\nDigite o valor da casa: ')) 
sal = float(input('Digite o salario do comprador: '))
anos = int(input('Digite em quantos anos ira pagar: '))

# Estrutura de Controle - Condional aninhada.
if (casa/(anos*12)) > ((sal*30)/100):
    print(f'Emprestimo nao aprovado, limite de 30% do sal: {(sal*30)/100}')
else:
    print(f'Pagamento Aprovado! Limite de 30%: {(sal*30)/100}')


