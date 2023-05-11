# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. 
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe um segundo número: '))

def comparaNumeros(num1, num2):
    if num1 > num2:
        return ('O primeiro valor é maior')
    elif num2 > num1:
        return ('O segundo valor é maior')
    else:
        return ('Não existe valor maior, os dois são iguais')
    
teste = print(comparaNumeros(numero1,numero2))


