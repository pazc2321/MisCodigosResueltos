#Inicializar variables
cantidadEjecutivos = 0
validacionCantEjecutivos = False
totalGerentesE = 0
totalAnalistasF = 0
antiguedad = 0

#Entrada de datos
while validacionCantEjecutivos == False:
    try:
        cantidadEjecutivos = int(input("Ingrese cantidad de ejecutivos a registrar: \n"))
        if cantidadEjecutivos <= 0:
            print("¡Transacción inválida! Ingresa un entero positivo para continuar.")
        else:
            if cantidadEjecutivos >= 1:
                validacionCantEjecutivos = True
    except ValueError:
        print("¡Transacción inválida! Ingresa un entero positivo para continuar.")

#Registro por ejecutivo
for i in range (cantidadEjecutivos):
    while True:
        try:
            codigoEmpleador = input(f"Ingrese el código del ejecutivo {i+1}: ")
            if len(codigoEmpleador) < 6:
                print("El código del ejecutivo debe tener al menos 6 caracteres.")
            elif (" ") in codigoEmpleador:
                print("No debe incluir espacios")
            else:
                break
        except ValueError:
            print("¡Transacción inválida! Ingresa un entero positivo para continuar.")    
    while True:
        try:
            antiguedad = int(input(f"Ingrese los años de experiencia del ejecutivo {i+1} en años: "))
            if antiguedad < 0:
                print("¡Error financiero! Ingresa un número entero positivo para la antigüedad.")
            else:
                if antiguedad > 3:
                    totalGerentesE += 1
                elif antiguedad <= 3:
                    totalAnalistasF += 1
                break
        except ValueError:
            print("¡Error financiero! Ingresa un número entero positivo para la antigüedad.")
#Salida
print(f"¡El banco cuenta con {totalGerentesE} Gerentes Ejecutivos y {totalAnalistasF} Analistas Financieros! ¡Operaciones autorizadas!")