#Importar
import diccionarios_y_funciones as funciones
import time

opc = 0
numServidores = 0
uptime = 0
carga = 0

#Lista de colección general
servidores = []

#Llamar función del menú
while True:
    funciones.menu_opciones()
    opc = int(input("Seleccione una opción del menú: "))

    #Agregar un servidor, Entrada de datos
    if opc == 1:
        try:
            numServidores = int(input("¿Cúantos servidores desea registrar?: "))
        except ValueError:
            print("Debe ingresar un número válido ")

        for i in range(numServidores):
            while True:
                try:
                    nombre = input(f"Ingrese el nombre del servidor {i+1}: ").lower()
                    if nombre.strip() == "":
                        print("El nombre no puede estar vacío")
                    elif " " in nombre:
                        print("El nombre no puede contener espacios.")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar carácteres válidos.")
            
            while True:
                try:
                    uptime = int(input(f"Núm. de días que el servidor '{nombre}' ha estado encendido [continuos]: "))
                    if uptime <= 0:
                        print("Debe ingresar un número mayor a 0.")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar un número entero positivo.")
            
            while True:
                try:
                    carga = float(input(f"Porcentaje del uso de la GPU del servidor '{nombre}': "))
                    if carga < 1 or carga > 100:
                        print("Debe ingresar un valor entre 1 y 100.")
                    else:
                        critico = False
                        break
                except ValueError:
                    print("Debe ingresar un número decimal válido")

            #Llamo a la funcion para agregar el diccionario; envío los datos con los parámetros.
            funciones.agregar_diccionario_servidor(servidores, nombre, uptime, carga)
            #Muestro el registro
            funciones.mostrar_datos_cargados(nombre, uptime, carga, critico)
            time.sleep(1)
    #Buscar servidor
    elif opc == 2:
        nombre = input("Ingresa el nombre del servidor a buscar: ").lower()
        funciones.buscar_servidores(nombre, servidores)
    #Eliminar servidor
    elif opc == 3:
        if not servidores:
            print("¡No hay servidores registrados!")
        else:
            nombre = input("Ingresa el nombre del servidor a eliminar: ").lower()
            funciones.eliminar_servidor(nombre, servidores)
    #Actualizar estados
    elif opc == 4:
        nombre = input("Ingrese el nombre del servidor a actualizar: ")
        funciones.actualizar_estado(nombre, servidores)
    #Mostrar servidores
    elif opc == 5:
        funciones.mostrar_lista_servidores(servidores)
    #Salir
    elif opc == 6:
        funciones.mensaje_salida()
        break