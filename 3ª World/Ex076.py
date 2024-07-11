# Ex076: Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos, na sequencia. No final, mostre uma listagem de precos, organizando os dados em forma tabular. 

tabela = ('Leite',10,'Bolacha',5,'Feijão',4,'Arroz',5)
for pos,c in enumerate(tabela):
    print(c,end=('.')*25 if pos%2==0 else '\n')

# Resolução do Professor:
listagem = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Canetas',22.30,
            'Livro',34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos%2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:<7.2f}')