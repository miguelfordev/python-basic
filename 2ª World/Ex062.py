# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

n = int(input('Digite um termo: '))
r = int(input('Digite a razao: '))
# d = n + (10-1)*r
op=''
while op != 'n':
        print(n)
        n=n+r
        op = input('Voce quer continuar a mostra o proximo termo: [s/n]').lower().strip()