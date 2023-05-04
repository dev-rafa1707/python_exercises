# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

listaAlunos = []

for i in range(4):
    aluno = str(input('Informe o nome do aluno:'))
    listaAlunos.append(aluno)

sorteado = random.choice(listaAlunos)



print(listaAlunos)
print(sorteado)



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