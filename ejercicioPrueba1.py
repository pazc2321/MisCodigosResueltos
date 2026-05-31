"""
Desarrolla un programa en Python que administre el registro del equipaje de mano para los pasajeros de 
un vuelo comercial de la aerolínea "VuelosChile". El programa debe validar correctamente todos los datos 
ingresados utilizando el control de excepciones para evitar caídas del sistema.
"""
#Inicialización de variables
totalEquipajes = 0
validacionEquipaje = False
validacionTicket = False
validacionPeso = True
equipajeBodega = 0
equipajeCabina = 0

#Cantidad de equipajes
print("=== Bienvenido a Vuelos Chile ===")

while validacionEquipaje == False:
    try:
        totalEquipajes = int(input("Ingrese la cantidad de equipajes: "))
        if totalEquipajes <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
        elif totalEquipajes >= 1:
            validacionEquipaje = True
    except ValueError:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar")
    
    #Registro por equipaje
    for i in range(totalEquipajes):
        while True:
            codigoTicket = input(f"Ingrese código de ticket de equipaje {i+1}: ").strip()
            if len(codigoTicket) < 5: #Validacion de Ticket
                print("Error: Debe tener al menos 5 caracteres")
            elif codigoTicket.isnumeric():
                print("Error: Debe incluir la menos una letra")
            else:
                break

        while True:
            pesoEquipaje = input(f"Ingrese peso del equipaje {i+1}[KG]:")
            validacionPeso = pesoEquipaje.isnumeric()

            if validacionPeso == False:
                print("¡Error de pesaje! Ingresa un número entero positivo para el peso.")
            else:
                pesoEquipaje = int(pesoEquipaje)
                if pesoEquipaje < 0:
                    print("¡Error de pesaje! Ingresa un número entero positivo para el peso.")
                else:
                    if pesoEquipaje > 10:
                        equipajeBodega = equipajeBodega + 1
                    elif pesoEquipaje <= 10:
                        equipajeCabina = equipajeCabina + 1
                    break
    print(f"¡El avión transportara {equipajeCabina} equipajes en Cabina e {equipajeBodega} equipajes en Bodega!¡Manifiesto de carga listo!")