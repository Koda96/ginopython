import verificacion

def ventas():
    montos = []
    dato = 0
    for monto in range(0,6):
        dato = int(input("Ingrese el monto de los meses"))
        if(verificacion.esEntero(dato) == True):
            montos.append(dato)
        else:
            print("Error, dato no compatible")
    print(montos)
    negativos(montos)
    actualiazda = negativos(montos)
    print (actualiazda)
    
def negativos(lista):
    for monto in lista:
        if (monto <= 0):
            lista.remove(monto)
    return lista