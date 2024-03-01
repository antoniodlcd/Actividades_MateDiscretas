'''
Ángel Antonio de la Cruz Díaz
Actividad 3
'''
import itertools

def evaluarProposicion(proposicion, valoresVerdad):
    for variable, valor in valoresVerdad.items():
        proposicion = proposicion.replace(variable, str(valor))

    return eval(proposicion)

def generarTabla(proposicion, variables):
    tabla = []
    valoresPosibles = itertools.product([True, False], repeat = len(variables))

    for valores in valoresPosibles:
        valoresVerdad = dict(zip(variables, valores))

        resultado = evaluarProposicion(proposicion, valoresVerdad)
        fila = {**valoresVerdad, 'Resultado': resultado}
        tabla.append(fila)

    return tabla

def mostrarTabla(tabla):
    print('P\tQ\rS\tResultado')
    print('---------------------')

    for fila in tabla:
        p = 'V' if fila['P'] else 'F'
        q = 'V' if fila['Q'] else 'F'
        s = 'V' if fila['S'] else 'F'
        resultado = 'V' if fila['Resultado'] else 'F'
        print(f'{p}\t{q}\t{s}\t{resultado}')


def main():
    proposicion = input('Ingresa la proposición > ')
    variables = ['P', 'Q', 'S']
    tabla = generarTabla(proposicion, variables)
    mostrarTabla(tabla)

main()