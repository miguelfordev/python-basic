#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trablhos do alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import shuffle
lista = [input('Digite o nome do aluno: ') for c in range(4)]
shuffle(lista)
print(f'A ordem de sorteio foi: {lista}')