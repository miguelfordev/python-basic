# Ex112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamda leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from pct112.utilidadesCeV.moedas import moeda
from pct112.utilidadesCeV.dados import dados

preço = dados.leiaDin('Digite o preço: R$')
moeda.resumo(preço, 35, 22, True)