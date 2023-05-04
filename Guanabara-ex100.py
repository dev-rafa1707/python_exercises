# Faça um programa que tenha uma lista chamada números e duas funções 
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
# e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre 
# todos os valores pares sorteados pela função anterior.

from random import random
from random import randint


lista = [1,2,3,4,5,6,7,8,9,10]
# listaa = [235,568,44,566,68,2,8,568,10,98]
# listab = [235,568,4444,566,68,2,8,568,10,98]

listaCinco = []

def sorteia(lista):
    for i in range(5):   
        listaCinco.append(randint(0,len(lista)-1))
        # listaCinco.append(randint(1,10))
    return listaCinco



def somaPar(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0: #Par
            contador += numero
    return contador


lista2 = sorteia(lista)
print(lista2)

print(somaPar(lista2))