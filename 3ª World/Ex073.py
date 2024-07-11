# Ex073: Crie uma tupa preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Apenas os 5 primeiros colocados. b) Os ultimos 4 colocados da tabela c) Uma lista com os times em ordem alfabetica. d) Em que posição na tabela está o time da Chapecoense(Bahia).

tabelaBrasileirão = 'Botafogo','Flamengo','Palmeiras','Gremio','Fluminense','Bragantino','Atletico PR','São Paulo','Cuiaba','Cruzeiro','Fortaleza','Inter','Atletico MG','Corinthians','Santos','Goiás','Bahia','Coritiba','América','Vasco'

print(f'Os 5 primeiros colocados são:')
for times in tabelaBrasileirão[:5]:
    print(times,end=', ' if times != tabelaBrasileirão[4] else '.')
print('\n')
print(f'Os 4 ultimos colocados são:')
for times in tabelaBrasileirão[-4:]:
    print(times,end=', ' if times != tabelaBrasileirão[-1] else '.')
print('\n')
print(f'Times em Ordem Alfabética: ')
for times in sorted(tabelaBrasileirão):
    print(times,end=', ' if times != tabelaBrasileirão[19] else '.')
print('\n')
print(f'Qual posição do Time do Bahia: ')
for pos,times in enumerate(tabelaBrasileirão):
    if times == 'Bahia':
        print(f'O Time do {times} se econtra na {pos+1}ª posição da tabela.')

# Resolução do professor: 

print(f'Lista de Times: {tabelaBrasileirão}')
print('-='*15)
print(f'Os 5 primeiros são {tabelaBrasileirão[0:5]}')
print('-='*15)
print(f'Os 4 ultimos são {tabelaBrasileirão[-4:]}')
print('-='*15)
print(f'Times em ordem Alfabetica: {sorted(tabelaBrasileirão)}')
print('-='*15)
print(f'O Bahia está na {tabelaBrasileirão.index("Bahia")+1} posição')