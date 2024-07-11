# Ex075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) Quantas vezes o apareceu o valor 9 b) Em que posicao foi digitado o primeiro valor 3 c) Quais foram os numeros pares.
tupla = ()
for c in range(4):
    valor = int(input(f'Digite o {c+1}º valor: '))
    tupla += (valor,)
print(f'O valor 9 apareceu: {tupla.count(9)} vezes.')
print(f'O primeiro valor 3 foi digitado na posição: {tupla.index(3)+1}')
print('Numeros Pares na Tupla: ')
for c in tupla:
    if c % 2==0:
        print(c,end=' ')

# Resolução do professor: 
núm= (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite outro numero: ')))
print(f'Voce digitou os valors {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado.')
for n in núm:
    if n%2==0:
        print(n, end='')