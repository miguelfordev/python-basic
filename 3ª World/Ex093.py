# Ex093: Crie um programa  que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
gols = []
jogador = {}
jogador["nome"] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for gol in range(partida):
    gols.append(int(input(f'Quantos gols na {gol+1}ª partida: ')))
jogador["gols"] = gols[:]
jogador["total"] = sum(jogador["gols"])
print('-='*25)
print(jogador)
print('-='*25)
for key,value in jogador.items():
    print(f'O campo {key} tem valor {value}')
print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {partida} partidas.')
for n,partidas in enumerate(jogador["gols"]):
    print(f'=> Na partida {n+1}, fez {partidas} gols.')
print(f'Foi um total de {jogador["total"]} gols')

# Resolução do Professor:
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')


