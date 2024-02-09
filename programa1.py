'''
Ángel Antonio de la Cruz Díaz FT. Fernándo Tiscareño Herrera
Función que verifica inicio y fin
07/02/2024 v1.0
'''


cadena = input("Introduzca su fórmula > ")

lista =[]
for i in (cadena):
    lista.append(i)


if ((lista[0].isalpha() or lista[0] == '(' or lista[0] == '¬' ) and ( lista[-1].isalpha() or lista[-1] == ')' )):
    print('La fórmula es FBF')
else:
    print('La fórmula no es FBF')
    