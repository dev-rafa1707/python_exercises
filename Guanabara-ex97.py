# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem 
# com tamanho adaptável.

def escrever(msg):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)


escrever('Carlos Rafael Sunhog Pacheco')
escrever('Bom dia')