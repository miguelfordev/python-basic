#Crie um algoritmo que leia um numero e mostre o seu dobro,triplo e raiz quadrada.

numero = float(input('\nDigite um numero: '))
print('='*100)
print(f'O dobro do numero {numero} e igual a {numero*2},',end=' ')
print(f'o triplo dele e igual a {numero*3}',end=' ')
print(f'e sua raiz quadrada e igual a {numero**(1/2):.2f}.\n')