# Ex089: Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
lista_alunos_notas = []
lista_controle = []
while True:
    lista_controle.append(input('Digite o nome do aluno: '))
    lista_controle.append(float(input('Digite a primeira nota: ')))
    lista_controle.append(float(input('Digite a segunda nota: ')))
    lista_controle.append((lista_controle[1]+lista_controle[2])/2)
    lista_alunos_notas.append(lista_controle[:])
    lista_controle.clear()
    r = str(input('Quer continuar? '))
    if r in 'nN':
        break
print('-='*15)
print('No.  NOME            MÉDIA')
print('--'*15)
for pos,aluno in enumerate(lista_alunos_notas):
    print(f'{pos} - {aluno[0]:<17} {aluno[3]:.1f}')
print('--'*15)
while True:
    res = str(input('Deseja mostrar a nota individual de alguem [S/N]? '))
    if res in 'nN':
        break
    else:
        resp = int(input('Qual o numero do aluno: '))
        print(f'Aluno: {lista_alunos_notas[resp][0]} - Nota 1: {lista_alunos_notas[resp][1]} e Nota 2: {lista_alunos_notas[resp][2]}.')
        print('--'*15)

# Resolução do Professor:
ficha = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')