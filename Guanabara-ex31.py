# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
#  e R$0,45 parta viagens mais longas.

distancia = float(input('Informe a distância da sua viagem:'))

if distancia <= 200:
    preco = distancia * .5
else:
    preco = distancia * .45

print(f'{preco:.2f}')
