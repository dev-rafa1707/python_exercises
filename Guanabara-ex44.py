# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o valor do produto:'))

print('Selecione 1 para pagamento à vista dinheiro/cheque: 10 de desconto')
print('Selecione 2 para pagamento à vista no cartão: 5 de desconto')
print('Selecione 3 para pagamento em até 2x no cartão: preço formal')
print('Selecione 4 para pagamento 3x ou mais no cartão: 20 de juros')


condicao = int(input('Informe a condição:'))

def calculaCondicao(preco, condicao):
    if condicao == 1:
        preco = 0.9 * preco
        return preco
    elif condicao == 2:
        preco = 0.95 * preco
        return preco
    elif condicao == 3:
        return preco
    elif condicao == 4:
        preco = 1.2 * preco
        return preco
    else:
        print('Opção inválida')

cliente = calculaCondicao(preco,condicao)
print(cliente)