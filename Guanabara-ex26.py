# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
# mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez 
# e em que posição ela aparece a última vez.

frase = str(input('Informe uma frase:')).strip().upper()
l = str(input('Informe a letra a ser procurada:')).upper()

print(frase)

quantidade = frase.count(l)
print(quantidade)

print('A primeira posição é',frase.find(l)+1)
print('A última posição é',frase.rfind(l)+1)