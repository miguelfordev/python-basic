"""             Python Mundo 3 - Variaveis Compostas - Tuplas
----------------------------------------------------------------------------------

lanche = ('hambuguer','suco','pizza','pudim)
               0         1      2       3

print(lanche[2]) -> pizza
print(lanche[0:2]) -> hambuguer, suco
print(lanche[1:]) -> suco, pizza, pudim
print(lanche[-1]) -> pudim
----------------------------------------------------------------------------------
Método/Função: (Comprimento da Tupla )
print(len(lanche)) -> 4
----------------------------------------------------------------------------------
Laços de Repetição: FOR
c -> é uma variavel simples que serve para salvar UMA informação dentro de um tamanho até terminar.
for c in lanche:
    print(c)
----------------------------------------------------------------------------------
OBS:                    As TUPLAS são IMUTÁVEIS!
----------------------------------------------------------------------------------
Exemplos:
lanche = 'hambuguer','suco','pizza','pudim -> Tuplas são criadas também sem parenteses

Ex01:
print(lanche[1]) -> Não é por que dentro do print é [] que vai deixar de ser Tupla, é só uma maneira de referenciar para o print.

Ex02:
lanche[1] = 'Refrigerante'
print(lanche[1]) -> ERROR 

Ex03: DADOS E POSIÇÃO
for cont in range(0,len(lanche)):
    print(f'Eu vou comer: {lanche[cont]} na posicao: {cont})

Ex04: DADOS E POSIÇÃO
for pos, comida in enumarate(lanche):
    print(f'Eu vou comer: {comida} na posição: {pos})

Ex05: COLOCANDO EM ORDEM:
lanche = ('hambuguer','suco','pizza','pudim','batata frita')
print(sorted(lanche)) -> Coloca em ordem, precisando transformar em Lista

Ex 06: MÉTODOS DO OBJETO TUPLA
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c) -> (5,8,1,2,2,5,4)
print(len(c)) -> 7
print(c.count(5)) -> Conta quantos vezes o numero 5 apareceu = 2
print(c.index(8)) - Mostra aonde esta a posição da primeira ocorrencia do parametro passado no caso o numero 8 = posição 1

pessoa = ('Gustavo',39,'M',99.88)
print(pessoa) -> Pode ter DADOS de TIPOS diferentes

del(pessoa) -> APAGA da memoria a Tupla inteira, não podendo deletar um só item.
"""

#Ex072: Cria um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

n = int(input('Digite um numero inteiro entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('COMANDO INVALIDO. Digite novamente: '))    
if n <= 20 or n >= 0:
    print(tupla[n])

# Resolução do professor: 

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente', end='')
print(f'Voce digitou o numero: {tupla[n]}')