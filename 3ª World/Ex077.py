# Ex077: Crie um programa que tenha uma tupla com varias palavras(nao usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.

tupla = ('Amanda','Lucas','Rodrigo','Evert','Miguel')
# vogais = ('a','e','i','o','u')
for pos,c in enumerate(tupla):
    print(f'Vogais de {tupla[pos]}:',end=' ')
    for c in tupla[pos]:
        if  c.lower() in 'aeiou':
            print(c,end=' ')
    print('\n')

# Resolução do Professor: 
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for p in palavras:
    print(f'/nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aáãeéêiíoóuú':
            print(letra, end=' ')