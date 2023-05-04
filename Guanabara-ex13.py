# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.



salario = float(input("Informe o valor do salário: "))
reajuste = float(input("Informe o valor do reajuste (em %): "))




def calcula(valor, indice):
    valor = valor + valor * (indice / 100)
    return valor


salarioNovo = calcula(salario, reajuste)

print(f"O salario antigo era {salario}, e o salario reajustado a {reajuste} % é de {salarioNovo}.")












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