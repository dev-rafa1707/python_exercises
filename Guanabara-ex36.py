# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorImovel = float(input('Informe o valor do imóvel:'))
salario = float(input('Informe o salario do comprador:'))
periodo = int(input('Informe a duração do contrato'))

prestacao = valorImovel / (periodo * 12)

if prestacao > salario * 30/100:
    print('Espréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO')