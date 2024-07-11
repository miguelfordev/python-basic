# Ex104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um número: ')

def leiaInt(msg: str) -> int:
    while True:
        try:
            num = input(msg)
            num_decimal = float(num)
            if num_decimal.is_integer():
                return int(num_decimal)
            return num_decimal
        except ValueError:
            print('ERROR, você digitou um caracter.')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# Resolução do Professor: 
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('(cor red)ERROR! Digite um número válido.(fechando cor red)')
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')