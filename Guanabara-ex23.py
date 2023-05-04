# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.

# numero = int(input('Informe um número:'))
# n = str(numero)
# print('Unidade:',n[3])
# print('Dezena:',n[2])
# print('Centena:',n[1])
# print('Milhar:',n[0])

numero = int(input('Informe um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade:',u)
print('Dezena:',d)
print('Centena:',c)
print('Milhar:',m)