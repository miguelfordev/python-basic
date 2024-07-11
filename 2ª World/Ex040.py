''' Desafio 40: Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0:
    REPROVADO
- Media entre 5.0 e 6.9:
    RECUPERACAO
- Media 7.0 ou superior:
    APROVADO
'''

# Entrada de dados
n1 = float(input('\nDigite a primeiro nota: '))
n2 = float(input('Digite a segunda nota: '))

#Estrututa de controle - condicional
if (n1+n2)/2 < 5.0:
    print('REPROVADO')
elif (n1+n2)/2 >= 5.0 and (n1+n2)/2 <= 6.9:
    print('RECUPERACAO')
else:
    print('Aprovado')