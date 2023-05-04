# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

lista = ['joao', 'maria', 'bruxa', 'guliver', 'gigante']
# ordem = []

# for i in range(len(lista)):
#     aluno = random.choice(lista)
#     ordem.append(aluno)
#     lista.remove(aluno)


# print(lista)
# print(ordem)


# =======================================================================

random.shuffle(lista)

print(lista)