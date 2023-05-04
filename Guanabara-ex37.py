# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.



numero = int(input('Informe um número: '))
print(''' Escolha uma das bases numéricas
[1] para binário
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Sua opção:'))

if opcao == 1:
    numero = bin(numero)
    print(numero[2:])
elif opcao == 2:
    numero = oct(numero)
    print(numero[2:])
elif opcao == 3:
    numero = hex(numero)
    print(numero[2:])
else:
    print('Opção inválida. Tente novamente.')