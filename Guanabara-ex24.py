# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga 
# se ela começa ou não com o nome "SAO".

cidade = str(input('Informe o nome da sua cidade de nascimento:'))
cidade = cidade.strip()

if cidade[0] == 's' or cidade[0] == 'S' and cidade[1] == 'a' or cidade[1] == 'A' and cidade[2] == 'o' or cidade[2] == 'O':
    print(True)
else:
    print(False)
