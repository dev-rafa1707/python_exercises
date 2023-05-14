# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

def calculaIMC(peso, altura):
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        return f'Abaixo do peso pois o IMC é {imc}'
    elif imc > 18.5 and imc < 25:
        return f'Peso ideal pois o IMC é {imc}'
    elif imc > 25 and imc < 30:
        return f'Sobrepeso pois o IMC é {imc}'
    elif imc > 30 and imc < 40:
        return f'Obesidade pois o IMC é {imc}'
    elif imc > 40:
        return f'Obesidade mórbida pois o IMC é {imc}'
    else:
        return f'Verifique os dados'

imc = print(calculaIMC(peso, altura))