'''Desafio 38: Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor e maior
- O segundo valor e maior
- Nao existe valor maior, os dois sao iguais
'''

# Entrada de dados
n1 = int(input('\nDigite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))

# Estrutura de controle - Condicional
if n1 > n2:
    print(f'O numero {n1} e maior que o numero {n2}')
elif n2 > n1:
    print(f'O  numero {n2} e maior que o numero {n1}')
elif n1 == n2:
    print(f'Os numeros sao iguais')
else:
    print(f'Operacao Invalida')