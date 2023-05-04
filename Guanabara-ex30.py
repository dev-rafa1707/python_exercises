# Exercício Python 030: Crie um programa que leia um número inteiro 
# e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Informe um número:'))

resto = numero % 2
if resto == 0:
    print('Numero par')
else:
    print('Numero impar')

