'''Crie um programa que leia dois valores e mostre um meno na tela:

[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos numeros
[5]Sair do programa

Seu programa devera realizar a operacao solicitada em cada caso.'''
from time import sleep
while True:
    print('-='*25)
    op = input('''          MENU
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos numeros
[5]Sair do programa

Digite a operacao a realizar: ''')
    while True:
        if op == '1':
            print('-='*25)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
            print(f'A soma dos valores e: {v1+v2}')
            print('-='*25)
            op2 = input('Voce quer continuar a realizar a operacao de [1]Soma [S/N]: ').upper().strip()
            if op2 == 'S':
                continue
            else:
                break
        if op == '2':
            print('-='*25)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
            print(f'A multiplicacao dos valores e: {v1*v2}')
            print('-='*25)
            op2 = input('Voce quer continuar a realizar a operacao de [2]Multiplicacao [S/N]: ').upper().strip()
            if op2 == 'S':
                continue
            else:
                break
        if op == '3':
            print('-='*25)
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
            if v1 > v2:
                print(f'O primeiro valor: {v1} e maior que o segundo: {v2}')
            else:
                print(f'O segundo valor: {v2} e maior que o primeiro: {v1}')
            print('-='*25)
            op2 = input('Voce quer continuar a realizar a operacao de [3]Maior [S/N]: ').upper().strip()
            if op2 == 'S':
                continue
            else:
                break
        if op == '4':
            print('Nao sei o que isso faz.')
            break
        if op == '5':
            print('Saindo do programa...')
            sleep(0.5)      
            break
    if op == '5':
        break
            
        

