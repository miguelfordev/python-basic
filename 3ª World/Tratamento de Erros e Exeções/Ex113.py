# Ex113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try: 
            n = str(input(msg))
            valor = int(n)
            ok = True
        except:
            print('Por favor digite um número válido.')
        if ok:
            break
    return valor

def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            m = str(input(msg)).replace(',','.')
            valor = float(m)
            ok = True
        except:
            print('Por favor digite um número válido.')
        if ok:
            break
    return valor

n = leiaInt('Digite um número inteiro: ')
print(n)

m = leiaFloat('Digite um número decimal: ')
print(m)

# Resolução do professor:
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')