# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso 
# de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

r1 = float(input('Lado 1 do triangulo: '))
r2 = float(input('Lado 2 do triangulo: '))
r3 = float(input('Lado 3 do triangulo: '))

def triangulo(r1,r2,r3):
    if r1 == r2 == r3:
        return 'Triângulo EQUILÁTERO'
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        if r1 == r2 or r1 == r3 or r2 == r3:
            return 'Triângulo ISÓSCELES'
        else:
            return 'Triângulo ESCALENO'
    else:
        return 'Essas retas não podem formar um triangulo'


triangulo = print(triangulo(r1,r2,r3))