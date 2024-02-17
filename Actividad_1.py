'''
Ángel Antonio de la Cruz Díaz
'''
nombre_archivo = 'proposiciones.txt'

with open(nombre_archivo, 'r') as archivo:
    print('Abriendo archivo...')
    numero_lineas = int (archivo.readline().strip())
    lineas = [archivo.readline().strip() for _ in range(numero_lineas)]

for linea in lineas:
    salida_1 = ''
    salida_2 = ''
    count = 0

    if (linea[0].isalpha() or linea[0] == "(" or linea[0] == "¬") and (linea[-1].isalpha() or linea[-1] == ")"):
        salida_1 = 'V'
    else:
        salida_1 = 'F'

    for char in linea:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        elif count < 0:
            break
    if count != 0:
        salida_2 = 'F'
    else:
        salida_2 = 'V'

    print(salida_1, salida_2)
    