# Ex095: Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
gols = []
jogador = {}
lista_jogadores = []
while True:
    jogador["nome"] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for gol in range(partida):
        gols.append(int(input(f'Quantos gols na {gol+1}ª partida: ')))
    jogador["gols"] = gols[:]
    jogador["total"] = sum(jogador["gols"])
    lista_jogadores.append(jogador.copy())
    gols.clear()
    r = str(input('Continue?'))
    if r in 'nN':
        break
print('-='*25)
print(f'cod nome     gols        total')
print('-'*45)
for cod,jogador in enumerate(lista_jogadores):
    print(f'{cod}-{jogador["nome"]} {jogador["gols"]} {jogador["total"]}')
print('-'*45)
while True:
    rps = int(input('Digite o codigo do jogador para saber dados? 999 interrompe. '))
    if rps == 999:
        break
    if rps < len(lista_jogadores):
        print(f'O jogador {lista_jogadores[rps]["nome"]} jogou {len(lista_jogadores[0]["gols"])} partidas.')
        for n,gols in enumerate(lista_jogadores[rps]["gols"]):
            print(f'=> Na partida {n+1}, fez {gols} gols.')
        print(f'Foi um total de {lista_jogadores[rps]["total"]} gols')
    else:    
        print('ERROR. Não existe esse jogador. Tente novamente')

# Resolução do Professor:
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')