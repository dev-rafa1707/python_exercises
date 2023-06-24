# Exercício Python 050: Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

def somarPares():
    numeros = []
    soma = 0
    for i in range(6):
        numero = int(input('Informe um numero inteiro: '))
        if numero % 2 == 0:
            soma = soma + numero
    return soma

soma = print(somarPares())
