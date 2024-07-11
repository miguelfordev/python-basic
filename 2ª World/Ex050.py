# Ex050: Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
soma=0
for c in range(1,7):
    n = int(input(f'Digite o {c} numero: '))
    if n%2==0:
        soma += n
print(soma)