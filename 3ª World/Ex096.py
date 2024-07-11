'''             Aula 20 - Funções Parte 1
------------------------------------------------------------
def lin():
    print("-"*30)


# Programa Principal:
lin()
print("     CURSO EM VIDEO      ")
lin()

def mensagem(msg):
    lin() ou print("-"*30)
    print(msg)
    lin() ou print("-"*30)


# Programa Principal:
mensagem('Sistema de Alunos')

def contador(*núm):
    print(núm)

    
# Programa Principal:    
contador(2,1,7)

def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

        
#Programa Principal:
valores = [7,2,5,0,4]
dobra(valores)
print(valores)
'''

# Ex096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(base: float,altura: float):
    a = base*altura
    return a

base = float(input('Digite a largura(m): '))
altura = float(input('Digite o comprimento(m): '))
print(f'A area é: {area(base,altura):.1f}m².')

# Resolução do Professor:
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos ')
print('-'*20)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
área(l,c)