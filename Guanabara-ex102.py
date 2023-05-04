# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um 
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

from asyncio.windows_events import NULL

# valor = int(input('Informe um número:'))


# def funcFatorial(num):
#     fatorial = 1
#     for num in range (1,num+1):
#         fatorial *= num
#     return fatorial


# print(funcFatorial(valor))






def fatorial(numero,logico):
    if logico == True:
        numFatorial = 1
        for numero in range(1,numero+1):
            numFatorial *= numero
        return numFatorial
    else:
        return NULL

print(fatorial(5,False))