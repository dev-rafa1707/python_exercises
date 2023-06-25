# Exercício Python 051: Desenvolva um programa que leia o primeiro termo 
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

def PA10termos(primeiroTermo, razao):
    pa = []
    termo = primeiroTermo
    pa.append(termo)
    for i in range (9):
        termo = termo + razao
        pa.append(termo)
    return(pa)

teste = print(PA10termos(primeiroTermo,razao))


