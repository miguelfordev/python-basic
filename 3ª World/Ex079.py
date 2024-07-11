# Ex079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_valores = []
while True:
    valor = ( int( input('Digite um valor: ') ) )
    if valor in lista_valores:
        print('ERROR, não é possível adicionar numeros repetidos.')
    else:
        lista_valores.append(valor)
    r = input('Continue?').upper().strip()
    if r != 'N' and r != 'S':
        while True:
            r = input('COMANDO INVALIDO. CONTINUE?').upper().strip()
            if r == 'S' or r == 'N':
                break
    if r == 'N':
        break
lista_valores.sort()
print(f'A lista de valores unicos digitados são: {lista_valores}')

# Resolução do Professor:

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não vou adicionar')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
números.sort()
print(f'Voce digitou os valores: {números}')