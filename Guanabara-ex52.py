# Exercício Python 052: Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo.

num = int(input("Informe um número inteiro: "))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Número primo")
else:
    print("Número não é primo")