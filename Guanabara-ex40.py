# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

def calculaMedia (nota1, nota2):
    media = (nota1+nota2) / 2
    if media < 5:
        return f'(A média é {media} e o aluno está REPROVADO)'
    elif media > 5 and media < 6.9:
        return f'(A média é {media} e o aluno está de RECUPERAÇÃO)'
    else:
        return f'(A média é {media} e o aluno está de APPROVADO)'


media = print(calculaMedia(nota1,nota2))
