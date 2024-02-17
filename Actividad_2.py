'''
Ángel Antonio de la Cruz Díaz
'''
def inicioFin(linea):
    # comprueba que el inicio y el fin de la fórmula sean correctos
    if (linea[0].isalpha() or linea[0] == "(" or linea[0] == "-"):
        if(linea[-1].isalpha() or linea[-1] == ")"):
            return True
        else:
            return False
    else:
        return False
        
def parentesis(linea):
    # comprueba que los paréntesis estén bien posicionados dentro de la fórmula
    count = 0
    for char in linea:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        elif count < 0:
            break
    if count != 0:
        return False
    else:
        return True

def lugar(linea):
    # comprueba que las proposiciones estén bien formuladas
    posicion = len(linea)

    for i in range(0, posicion):
        if (linea[i].isalpha()):
            if (posicion > 1):
                if (i == 0):
                    if (linea[i+1] == ')' or linea[i+1] == '>' or linea[i+1] == '&' or linea[i+1] == '|' or linea[i+1] == '='):
                        return True
                else:
                    if (linea[i+1] == ')' or linea[i+1] == '>' or linea[i+1] == '&' or linea[i+1] == '|' or linea[i+1] == '=') and (linea[i-1] == '(' or linea[i-1] == '-' or linea[i-1] == '&' or linea[i-1] == '|' or linea[i-1] == '>' or linea[i-1] == '='):
                        return True
            else:
                return True
    return False

def conector(linea):
    # comprueba que los conectores estén bien posicionados dentro de la fórmula
    conectores = ['>', '&', '|', '=', '-']
    posicion = len(linea)

    for i in range(0, posicion):
        if (posicion > 1):
            if (linea[i] == '-'):
                if (i == 0):
                    if (linea[i+1] == '-' or linea[i+1] == '(' or linea[i+1].isalpha()):
                        return True
                else:
                    if (linea[i+1] == '-' or linea[i+1] == '(' or linea[i+1].isalpha()) and (not(linea[i-1].isalpha()) or not(linea[i-1] == ')')):
                        return True
                    else:
                        return False
            else: 
                if (linea[i] in conectores):
                    if (linea[i+1].isalpha() or linea[i+1] == '(' or linea[i+1] == '-') and (linea[i-1].isalpha() or linea[i-1] == ')'):
                        print('hola')
                        return True
                    else:
                        return False
                    
    return True


nombre_archivo = 'proposiciones.txt'

with open(nombre_archivo, 'r') as archivo:
    print('Abriendo archivo...')
    numero_lineas = int(archivo.readline().strip())
    lineas = [archivo.readline().strip() for _ in range(numero_lineas)]

for linea in lineas:
    salida = ''

    if inicioFin(linea):

        salida += 'V '
    else:
        salida += 'F '
    
    if parentesis(linea):
        salida += 'V '
    else:
        salida += 'F '
    
    if lugar(linea):
        salida += 'V '
    else:
        salida += 'F '
    
    if conector(linea):
        salida += 'V '
    else:
        salida += 'F '
    print(salida)

