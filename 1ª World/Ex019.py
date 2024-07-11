#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
alunos = [input('Digite o nome do aluno: ') for c in range(4)]
print(f'O sorteado foi: {random.choice(alunos)}')