# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoNascimento = int(input('Informe seu ano de nascimento: '))

anoAtual = date.today().year

def alistamentoMilitar (anoNascto):
    global anoAtual
    if anoAtual - anoNascto > 18:
        return (f'Seu alistamento já ocorreu há {(anoAtual - anoNascto) - 18} anos')
    elif anoAtual - anoNascto < 18:
        # return(f'Seu alistamento vai ocorrer em {-1 * ((anoAtual - anoNascto) - 18)} anos')
        return(f'Seu alistamento vai ocorrer em {anoNascto + 18 - anoAtual} anos')
    else:
        return ('Seu alistamento ocorre esse ano. Aliste-se já')

teste = print(alistamentoMilitar(anoNascimento))
