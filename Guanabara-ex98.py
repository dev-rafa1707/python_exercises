# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio,fim,passo):
    for i in range (1,11):
        print(i)
    
    for i in range(10,-2,-2):
        print(i)



contador(1,10,1)