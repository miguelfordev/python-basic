''' Desenvolva um programa que leia o comprimento de tres retas e diga ao susuario se elas podem ou nao formar um triangulo.
'''

r = [int(input(f'Digite {x+1} reta: ')) for x in range(3)]
if r[0]<r[1]+r[2] and r[1]<r[0]+r[2] and r[2]<r[0]+r[1]:
    print('\33[0;35;45mpossivel fomar triangulo')
else:
   print('nao e possivel formar triangulo')

# \033[m <- escape saquence/padrao ANSI
# \033[0:33:44m <- colocando cor de fundo no terminal
#     style:text:backg
# style:
# 0 <- None
# 1 <- bold/negrito
# 4 <- underline/sublinhado
# 7 <- negative/inversao de cores

# text:
# 30 <- white 
# 31 <- red
# 32 <- green
# 33 <- yellow
# 34 <- blue
# 35 <- pink
# 36 <- cian
# 37 <- gray

# back:
# 40 <- white 
# 41 <- red
# 42 <- green
# 43 <- yellow
# 44 <- blue
# 45 <- pink
# 46 <- cian
# 47 <- gray