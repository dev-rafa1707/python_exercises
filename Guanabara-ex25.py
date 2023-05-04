# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome


nome = str(input('Informe seu nome:')).strip()


nome = nome.upper()
resposta = 'SILVA' in nome
print(resposta)