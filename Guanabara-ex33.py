# Exercício Python 033: Faça um programa que leia três números 
# e mostre qual é o maior e qual é o menor.

num1 = int(input('Informe o 1o. numero:'))
num2 = int(input('Informe o 2o. numero:'))
num3 = int(input('Informe o 3o. numero:'))

maior = num1
menor =  num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3

print('O maior número é:', maior)
print('O menor número é:', menor)