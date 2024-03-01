'''
Ángel Antonio de la Cruz Díaz
Actividad 5
28/02/2024
'''

def validarCaracteres(proposicion):
    caracteresValidos = set('()&|-')

    for caracter in proposicion:
        if caracter not in caracteresValidos and not caracter.isalpha():
            return False
    return True

def fnc(proposicion):
    caracteres = proposicion.split('&')
    validos = ['|', '(', ')']

    for caracter in caracteres:
        
        if all(caracter in caracteres for valido in validos):
            continue
        else:
            return False
        
def fnd(proposicion):
    caracteres = proposicion.split('|')
    validos = ['&', '(', ')']

    for caracter in caracteres:
        
        if all(caracter in caracteres for valido in validos):
            continue
        else:
            return False

def main():
    proposicion = input('Ingrese la preposición > ')

    if len(proposicion) <= 20:
        if not(validarCaracteres(proposicion)):
            print('Hay caracteres inválidos')
        elif fnc(proposicion):
            print('Es FNC')
        elif fnd(proposicion):
            print('Es FND')
        else:
            print('Sólo es FN')
    else:
        print('Número de caractéres inválido')

main()