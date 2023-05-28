# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random
from random import randint


print('Suas opções')
print('[1] para pedra')
print('[2] para papel')
print('[3] para tesoura')

jogador = int(input('Informe sua jogada: '))


def janKenPo(jogador):
    computador = random.randint(1,3)

    if computador == 1:
        print('Computador escolheu pedra')
    elif computador == 2:
        print('Computador escolheu papel')
    elif computador == 3:
        print('Computador escolheu tesoura')   


    if jogador == computador:
        return('Empate')
    elif jogador == 1 and computador == 2:
        return('Você perdeu')
    elif jogador == 1 and computador == 3:
        return('Você ganhou')
    elif jogador == 2 and computador == 1:
        return('Você ganhou')
    elif jogador == 2 and computador == 3:
        return('Você perdeu')
    elif jogador == 3 and computador == 1:
        return('Você perdeu')
    elif jogador == 3 and computador == 2:
        return('Você ganhou')
    
jogada = print(janKenPo(jogador))