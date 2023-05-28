# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva
#  para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

import time

def contagemRegressiva(contador):
    while contador > 0:
        print(contador)
        time.sleep(1)
        contador -= 1

contagem = contagemRegressiva(10)

