# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input("Informe a altura em m²: "))
largura = float(input("Informe a largura em m²: "))


def pintura(a,l):
    area = a * l
    qdadeLitros = area / 2
    print(area)
    print(qdadeLitros)


pintura(altura,largura)
