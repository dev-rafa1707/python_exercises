# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input('Informe seu nome:'))
nome = nome.strip()
nome = list(nome.split(' '))
print(nome)
print(nome[0])
print(nome[-1])

