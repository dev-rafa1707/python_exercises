# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input("Informe o preço do produto: "))


def desconto(valor):
    valor = 0.95 * valor
    return valor


preçoNovo = desconto(preço)
print(preçoNovo)

print("Esse é o preço antigo:", preço)
print("Esse é o preço novo:", preçoNovo)
print("O preço antes do desconto era de {} reais, e com o desconto, o valor ficou {} reais.".format(preço, preçoNovo))
print(f"O valor antes do desconto era de {preço} reais e com o desconto ficou {preçoNovo} reais.")
print("O valor sem desconto era de %d, e com o desconto ficou por %d" %(preço,preçoNovo))
print("O valor do item com desconto foi de: %.6f." %preçoNovo)








# print(num,"é um número, enquanto",string,"é uma string!")
# print("{0} é um número, enquanto {1} é uma string!".format(num,string))
# print("%d é um número, enquanto %s é uma string!" %(num,string))
# print("Número com vírgula: %.2f!" %num)