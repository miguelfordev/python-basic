# Ex110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from pct110 import moeda

preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 50, 15, True)

