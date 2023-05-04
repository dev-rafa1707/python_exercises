# Crie um programa que tenha uma função chamada voto() que vai receber 
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


anoNacimento = int(input('Informe o ano de seu nascimento: '))


def voto(ano):
    anoCorrente = 2022
    if anoCorrente - ano < 16:
        return('Voto NEGADO.')
    elif anoCorrente - ano >= 16 and anoCorrente - ano < 18:
        return('Voto OPCIONAL.')
    elif anoCorrente - ano >= 18:
        return('Voto OBRIGATORIO.')


print(voto(anoNacimento))