# Ex083: Crie um programa onde o usuário digite uma expressão qualquer que use paraênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 
lista=[]
expressão = (input('Digite a expressão: '))
cont = 0
while True:
    lista.append(expressão[cont])
    cont+=1
    if cont == len(expressão):
        break
cont1=0
cont2=0
for c in lista:
    if c == '(':
        cont1+=1
    if c == ')':
        cont2+=1
if (cont1+cont2)%2==0:
    print('Operação Válida.')
else:
    print('Operação Invalida.')

# Resolução do Professor:
expr = str(input('Digite a expressão: '))
pilha=[]
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressao está inválida!')