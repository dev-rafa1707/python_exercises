# Exercício Python 053: Crie um programa que leia uma frase qualquer 
# e diga se ela é um palíndromo, desconsiderando os espaços.

def verificaPalindromo(string):
    string = string
    stringInvertida = string[::-1]
    if string == stringInvertida:
        return f'True'
    else:
        return f'False'
    
palavra = 'burro'
print(verificaPalindromo(palavra))
