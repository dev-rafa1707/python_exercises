# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
#  e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Lado 1 do triangulo'))
r2 = float(input('Lado 2 do triangulo'))
r3 = float(input('Lado 3 do triangulo'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triangulo')
else:
    print('Essas retas não podem formar um triangulo')