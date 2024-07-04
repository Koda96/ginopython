import validaciondiccionario

empleados = [
    {
        "nombre": "Juan Pérez",
        "edad": 30,
        "sueldo": 1500000,
        "cargas_familiares": [
            {"parentesco": "Esposa", "nombre": "Ana Gómez"},
            {"parentesco": "Hijo", "nombre": "Pedro Pérez"}
        ]
    },
    {
        "nombre": "María López",
        "edad": 40,
        "sueldo": -2000000,
        "cargas_familiares": [
            {"parentesco": "Hija", "nombre": "Laura López"}
        ]
    },
    {
        "nombre": "Carlos Fuentes",
        "edad": 25,
        "sueldo": 1200000,
        "cargas_familiares": []
    },
    {
        "nombre": "Elmoco Largo",
        "edad": 88,
        "sueldo": 1200000,
        "cargas_familiares": []
    },
    {
        "nombre": "Esteban Quito",
        "edad": 25,
        "sueldo": 1200000,
        "cargas_familiares": [
            {"parentesco": 40, "nombre": "Laura López"}
        ]
    }
]
    
def imprimir_empleados(empleados):
    for empleado in empleados:
        print("\n")
        print("Nombre: {}".format(empleado['nombre']))
        print("Edad: {}".format(empleado['edad']))
        print("Sueldo: {}".format(empleado['sueldo']))
        print("Cargas Familiares: ")
        for carga in empleado["cargas_familiares"]:
            print("Parentesco: {}".format(carga['parentesco']))
            print("Nombre de carga: {}".format(carga['nombre']))
            
def run():
    return validaciondiccionario.validar_empleados(empleados)
        