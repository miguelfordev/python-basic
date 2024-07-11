# Ex103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O prorgama deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    if nome == '':
        jogador = '<desconhecido>'
        resultado = gols
        if gols == '':
            resultado = 0
    else:
        resultado = gols
        jogador = nome
    return jogador,resultado


nome_jogador = input('Digite o nome do jogador: ')
saldo_gols = input('Digite o saldo de gols: ')
jogador, gols = ficha(nome_jogador,saldo_gols)
print(f'O jogador {jogador} fez {gols} gols.')


# Resolução do Professor:
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)