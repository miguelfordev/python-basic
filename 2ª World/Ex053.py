# Ex053: Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

f = input('Digite a frase: ').strip().upper()
p = f.split()
j = ''.join(p)
#i=''
i=j[::-1]
# for l in range(len(j)-1,-1,-1):
    # i+=j[l]
if i == j:
    print('palindromo')
else:
    print('nao e palindromo')