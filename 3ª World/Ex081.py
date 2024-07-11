# Ex081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) Quantos números foram digitados. b) A lista de valores, ordenada de forma decrescente. c) Se o valor 5 foi digitado e está ou não na lista.
lista:int = []
c:int = 0
while True:
    lista.append(int(input(f'Digite um valor: ')))
    c += 1
    resp = str(input('Quer continuar [S/N]? <- ')).upper().strip()
    if resp == 'N':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'A Lista Ordenada Descrescente: {lista}. Total de números digitados: {c}')
if 5 in lista:
    print(f'O valor 5 foi digitado e sua primeira ocorrencia esta na posição da lista: {lista.index(5)}ª posição')
else:
    print('O valor 5 não foi digitado.')

# Resolução do Professor:
valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Qur continuar? '))
    if resp in 'Nn':
        break
print(f'Voce digitou: {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')