'''
Ángel Antonio de la Cruz Díaz FT. Fernándo Tiscareño Herrera
Función que verifica los paréntesis de una función
07/02/2024 v1.0
'''

cadena = input("Introduzca su fórmula > ")

lista =[]
for i in (cadena):
    lista.append(i)


if ((lista[0].isalpha() or lista[0] == '(' or lista[0] == '¬' ) and ( lista[-1].isalpha() or lista[-1] == ')' )):
    for item in (cadena):
        if (item == '(' or item == ')'):
            if (item == '('):
                
    
    print('La fórmula es FBF')
else:
    print('La fórmula no es FBF')
    