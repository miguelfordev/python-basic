''' Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais o aumento e de 15%.
'''

sal = float(input('Digite o salario do funcionario: '))

if sal > 1250:
    print(f'Novo salario: {sal+(sal*10)/100}')
else:
    print(f'Novo salario 2: {sal+(sal*15)/100}')