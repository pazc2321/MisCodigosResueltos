"""
Construya un programa en Python que permita gestionar un sistema de arriendo 
y disponibilidad de bicicletas públicas mediante un menú interactivo. 
El sistema inicia la jornada con 25 bicicletas disponibles en la estación central.
"""
opcion = 0
bicicletasDisponibles = 25
bicicletasArrendadas = 0
devolverBicicletas = 0
viajesActivos = 0

print("¡Bienvenido al sistema de gestión de Eco-Bicis Urbanas")

while opcion != 5:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Bicicletas disponibles")
    print("2. Arrendar bicicletas") #Salida
    print("3. Devolver bicicletas") #Entrada
    print("4. Historial de viajes activos")
    print("5. Salir")
    opcion = int(input("Seleccione una opción del menú: "))

    if opcion == 1:
        print("\n-- Bicicletas disponibles --")
        print(f"Cantidad de bicicletas disponibles: {bicicletasDisponibles}\n")

    elif opcion == 2:
        print("\n-- Arrendar Bicicletas --")
        try:
            bicicletasArrendadas = int(input("Ingrese la cantidad de bicicletas que desea arrendar: "))
            if bicicletasArrendadas < 0:
                print("Debe ingresar una cantidad válida.\n")
            elif bicicletasArrendadas > bicicletasDisponibles:
                print(f"Sólo hay {bicicletasDisponibles} bicicletas disponibles para arrendar. Intente nuevamente.\n")
            else:
                print(f"Arrendaste {bicicletasArrendadas} con éxito.\n")
                bicicletasDisponibles = bicicletasDisponibles - bicicletasArrendadas #Salida
                viajesActivos = viajesActivos + bicicletasArrendadas
        except ValueError:
            print("Error: Debe ingresar una cantidad válida\n")

    elif opcion == 3:
        print("\n-- Devolver Bicicletas --")
        try:
            devolverBicicletas = int(input("Ingrese la cantidad de bicicletas que desea devolver: "))
            if devolverBicicletas <= 0:
                print("Debes devolver al menos 1 bicicleta.\n")
            elif (devolverBicicletas + bicicletasDisponibles) > 25:
                print("La capacidad máxima de bicicletas es 25. Intente nuevamente\n")
                devolverBicicletas = 0
            else:
                print(f"Devolviste {devolverBicicletas} con éxito.\n")
                bicicletasDisponibles = bicicletasDisponibles + devolverBicicletas
                viajesActivos = viajesActivos - devolverBicicletas
        except ValueError:
            print("Debe ingresar una cantidad válida de bicicletas\n")

    elif opcion == 4:
        print("\n-- Historial de viajes activos --")
        print(f"Actualmente hay {viajesActivos} bicicletas en ruta.\n")

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
    else:
        print("Porfavor elija una opción válida del menú\n")