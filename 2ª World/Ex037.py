'''Desafio 37: Escreva um programa que leia um numero inteiro qualquer e preca para o usuario escolher qual sera a base de conversao:
- 1 para binario
- 2 para octal
- 3 para hexadecimal
'''
# Entrada de dados
n = int(input('\nDigite um numero inteiro: '))
r = int(input('''Digite para saber se o numero digitado e: 
1-Binario 
2-Octal 
3-Hexadecimal: '''))

# Estrutura de Controle - Condicional
if r == 1:
    print(bin(n))
elif r == 2:
    print(oct(n))
elif r == 3:
    print(hex(n))
else:
    print('Resposta errada. Repita o programa.')