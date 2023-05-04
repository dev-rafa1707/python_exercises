# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

qdadeKM = float(input('Informe a quantidade de Km percorridos:'))
qdadeDias = int(input('Informe a quantidade de Dias:'))

diaria = 60
valorKM = .15

valor = qdadeDias * diaria + qdadeKM * valorKM
print('O valor a pagar é:', valor)









# print("Esse é o preço antigo:", preço)
# print("Esse é o preço novo:", preçoNovo)
# print("O preço antes do desconto era de {} reais, e com o desconto, o valor ficou {} reais.".format(preço, preçoNovo))
# print(f"O valor antes do desconto era de {preço} reais e com o desconto ficou {preçoNovo} reais.")
# print("O valor sem desconto era de %d, e com o desconto ficou por %d" %(preço,preçoNovo))
# print("O valor do item com desconto foi de: %.6f." %preçoNovo)


# print(num,"é um número, enquanto",string,"é uma string!")
# print("{0} é um número, enquanto {1} é uma string!".format(num,string))
# print("%d é um número, enquanto %s é uma string!" %(num,string))
# print("Número com vírgula: %.2f!" %num)