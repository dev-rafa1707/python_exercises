# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero = int(random.randint(0,5))
# print('numero',numero)
print('Adivinhe um número entre 0 e 5:')
aposta = int(input())

if numero == aposta:
    print('Você ganhou')
else:
    print('Você perdeu')

