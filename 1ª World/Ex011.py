#Faca um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m**2

larg = float(input('\nDigite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
print('='*100)
print(f'A area a ser pintada e de {larg*alt} m2, e a quantidade em litros de tinta necessaria e: {(larg*alt)/2} litros.\n')