# Ex097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex: escreva('Olá, Mundo!') Saida: ~~~~~~~~~ Olá, Mundo! ~~~~~~~~~

def escreva(txt):
    x = len(txt)+2
    print('~'*x)
    print(f' {txt:^} ')
    print('~'*x)

txt = str(input('Digite uma mensagem: '))
escreva(txt)

# Resolução do Professor:
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')