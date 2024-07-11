'''                 Estrutura de Repeticao - While
---------------------------------------------------------------------

Exemplos com For:
    for c in range(1,10):
        print(c) <- 1,2,3,4,5,6,7,8,9
    
Exemplos com While:
    c=1
    while c<10:
        print(c) <- 1,2,3,4,5,6,7,8,9
        c+=1
'''

# Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente ate ter um valor correto.

sexo = str(input('Digite o sexo: [M/F]')).lower().strip()

while sexo not in 'mf':
    sexo = str(input('Comando invalido. Digite novamente: [M/F] ')).lower().strip()