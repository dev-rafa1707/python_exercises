# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

lista = [1,11111112,3,4,5,6,7,8,999,10]
lista2 = [235,568,44,566,68,2,8,568,10,98]
lista3 = [235,568,4444,566,68,2,8,568,10,98]


def maior(parametro):
    maiorValor = parametro[0]
    for i in range(len(parametro)):
        if parametro[i] > maiorValor:
            maiorValor = parametro[i]
    return maiorValor


print(maior(lista))
print(maior(lista2))
print(maior(lista3))
