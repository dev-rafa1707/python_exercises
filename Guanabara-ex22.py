# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo:'))
nome = nome.strip()
maiusculas = nome.upper()
minusculas = nome.lower()
qdade = len(nome) - nome.count(' ')

print(maiusculas)
print(minusculas)
print(qdade)
print(nome.find(' '))