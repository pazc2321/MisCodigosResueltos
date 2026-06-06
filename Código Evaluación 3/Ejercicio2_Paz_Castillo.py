#Inicializar variables
opcion = 0
citasDisponibles = 40
capacidadMaxCitas = 40
historialReservas = 0
cancelarCitas = 0
citasProgramadas = 0

#Bienvenida
print("¡Bienvenido al sistema de gestión de citas de la Clínica San Lucas!")
while opcion != 5:
    try:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Citas disponibles")
        print("2. Programar cita")
        print("3. Cancelar cita")
        print("4. Historial de citas")
        print("5. Salir")

        opcion = int(input("Seleccione una opción del menú: "))
        if opcion == 1:
            print(f"\nHay {citasDisponibles} citas disponibles.\n")
            if citasDisponibles == 0:
                print("\n¡Lo sentimos! No hay citas disponibles.\n")
        elif opcion == 2:
            try:
                citasProgramadas = int(input("¿Cuántas citas desea programar?"))
                if citasProgramadas <= 0:
                    print("Debe programar al menos una cita.")
                elif citasProgramadas > citasDisponibles:
                    print(f"Sólo hay {citasDisponibles}. Intente de nuevo.")
                else:
                    print(f"\nProgramó {citasProgramadas} citas correctamente.\n")
                    citasDisponibles = citasDisponibles - citasProgramadas
                    historialReservas = historialReservas + citasProgramadas
            except ValueError:
                print("Error: Debe ingresar un número entero positivo de citas a programar.")
        elif opcion == 3:
            try:
                cancelarCitas = int(input("¿Cúantas citas desea cancelar?"))
                if cancelarCitas <= 0:
                    print("Debe cancelar al menos una cita.")
                elif (cancelarCitas + citasDisponibles) > capacidadMaxCitas:
                    print("No puedes cancelar más citas que la capacidad máxima de citas.")
                else:
                    print(f"\nCanceló {cancelarCitas} citas correctamente.\n")
                    citasDisponibles = citasDisponibles + cancelarCitas
                    historialReservas = historialReservas - cancelarCitas
            except ValueError:
                print("Error: Debe ingresar un número entero positivo de citas a cancelar.")
        elif opcion == 4:
            print(f"\nHa agendado {historialReservas} citas durante la sesión actual.\n")
        elif opcion == 5:
            print("\nGracias por utilizar nuestro software, hasta la próxima.\n")
            break
        else:
            print("Porfavor, ingrese una opción válida del menú")
    except ValueError:
        print("Porfavor, ingrese una opción válida del menú")