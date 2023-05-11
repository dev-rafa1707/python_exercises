# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que 
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER


from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Informe o ano de nascimento: '))

def calculaCategoria (anoAtual, anoNascimento):
    categoria = (anoAtual- anoNascimento)
    if categoria < 9:
        return f'(A idade é {categoria} e o atleta é da categoria MIRIM)'
    elif categoria > 9 and categoria < 14:
        return f'(A idade é {categoria} e o atleta é da categoria INFANTIL)'
    elif categoria > 14 and categoria < 19:
        return f'(A idade é {categoria} e o atleta é da categoria JUNIOR)'
    elif categoria > 14 and categoria < 25:
        return f'(A idade é {categoria} e o atleta é da categoria SÊNIOR)'
    else:
        return f'(A idade é {categoria} e o atleta é da categoria MASTER)'


categoria = print(calculaCategoria(anoAtual, anoNascimento))