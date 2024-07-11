# Ex056: Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa, mostre: a media de idade do grupo, nome do homem mais velho, quantas mulheres tem menos de 20 anos.
soma=0
nMaior=''
maior=0
nMenor=0
for c in range(4):
    n = str(input('Digite o nome da pessoa: ')).lower().strip()
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo: ').lower().strip()
    soma += i
    if s == 'm' and i > maior:
        maior = i
        nMaior = n
    if s == 'f' and i < 20:
        nMenor +=1
print(f'Media de idade do grupo: {soma/4:.2f} anos, Homem mais velho: {nMaior}, Mulheres com menos de 20: {nMenor} mulheres.')