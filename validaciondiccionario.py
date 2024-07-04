def validar_empleados(empleados):
    
    empleados_validos = []
    
    for empleado in empleados:
        nombre = empleado["nombre"]
        edad = empleado["edad"]
        sueldo = empleado["sueldo"]
        cargas_familiares = empleado["cargas_familiares"]
        
        #Validar Nombre:
        if not isinstance(nombre, str):
            print("({})Error, el nombre debe ser una cadena de texto, omitiendo dato".format(nombre))
            continue
        
        #Validar Edad:
        if not isinstance(edad, int) or not (18 <= edad <= 65):
            print("({})Error, la edad tiene que ser entre 18 y 65 años y ademas un numero entero, omitiendo dato (Dato erroneo {})".format(nombre,edad))
            continue
        
        #Validar sueldo:
        if not isinstance(sueldo, int) or isinstance(sueldo, float) or sueldo <=0:
            print("({})Error, el sueldo es negativo o no es un numero, omitiendo dato (Dato erroneo {})".format(nombre,sueldo))
            continue
        
        #Validar Cargas Familiares:
        cargas_validas = True
        for carga in cargas_familiares:
            parentesco = carga["parentesco"]
            nombre_carga = carga["nombre"]
            if not isinstance(parentesco, str) or not isinstance(nombre_carga, str):
                cargas_validas = False
                print("({})Error, el nombre o el parentesco tienen que ser cadenas de texto, omitiendo dato (Dato erroneo {})".format(nombre,parentesco))
                break
            
  
        if not cargas_validas:
            continue
            
        
        empleados_validos.append(empleado)

    return empleados_validos