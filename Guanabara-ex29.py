# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.


velocidade = int(input('Informe a velocidade do veículo:'))
limite = 80

if velocidade > limite:
    print('O veículo foi multado.')
else:
    print('A velocidade está de acordo com o limite.')

multa = (velocidade - limite) * 7
print('O valor da multa é:', multa)

