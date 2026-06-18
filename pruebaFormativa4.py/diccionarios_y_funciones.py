"""
-- INSTRUCCION --
Debo crear un 'Sistema de control de estado de servidores'.

Su objetivo es ser un programa que te permita agregar, buscar o eliminar
servidores según lo requerido.

Primordialmente el programa permite actualizar y mostrar los servidores y
sus estados actuales.

Para almacenar los servidores: Cada servidor es un diccionario individual. 
Cada diccionario debe guardarse dentro de una lista, la cual será la 
"colección general".

    - El programa comienza con la lista VACIA y se llenará con los registros del usuario.

    - El programa debe tener un menú infinito hasta que el usuario elija salir.
"""

#0. Función que muestra el menú
def menu_opciones():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar servidor") #OK
    print("2. Buscar servidor") 
    print("3. Eliminar servidor")
    print("4. Actualizar estados")
    print("5. Mostrar servidores") #OK
    print("6. Salir") #OK

#1. Función para crear y guardar los servidores/diccionarios en la lista
def agregar_diccionario_servidor(servidores, nombre, uptime, carga):
   servidor = {
        "nombre":nombre,
        "uptime":uptime,
        "carga":carga,
        "critico": False, #Predeterminado
    }
   servidores.append(servidor) #Aquí se guarda en la lista principal

#1.1 Función para mostrar los datos registrador en pantalla
def mostrar_datos_cargados(nombre, uptime, carga, critico):
    print("\n")
    print("="*45)
    print(f"DATOS DEL SERVIDOR CARGADOS EN EL SISTEMA: ")
    print("-"*45)
    print(f"Nombre: {nombre}")
    print(f"Uptime (Días): {uptime}")
    print(f"Uso del GPU (%): {carga}%")
    print(f"Estado crítico: {critico}")
    print("="*45)
    print(f"\n-- Registro del servidor '{nombre}' completado correctamente. --\n")

#2. Función para buscar servidores registrados
#Debe permitir buscarlos por su nombre
def buscar_servidores(nombre, servidores):
    for servidor in servidores: #Para recorrer la lista
        if servidor["nombre"].lower () == nombre.lower():
            print(f"Se ha encontrado el servidor: '{servidor}'")
            break
        else:
            print(f"No existe registro del servidor '{nombre}' en nuestra base de datos.")

#3. Función para eliminar un servidor
def eliminar_servidor(nombre, servidores):
    for servidor in servidores: #Para recorrer la lista
        if servidor["nombre"].lower() == nombre.lower():
            servidores.remove(servidor)
            print("Servidor eliminado correctamente.")
            break  
        else:      
            print(f"No existe registro del servidor '{nombre}' en nuestra base de datos.")

#4. Función para actualizar estado del servidor
def actualizar_estado(nombre, servidores):
    for servidor in servidores:
        if servidor["nombre"].lower() == nombre.lower():
            try:
                carga = float(input(f"Porcentaje del uso de la GPU del servidor '{nombre}': "))
                if carga < 1 or carga > 100:
                    print("Debe ingresar un valor entre 1 y 100.")
                else:
                    if carga >= 70:
                        print("Estado del servidor actualizado.")
                        servidor["carga"] = carga
                        servidor["critico"] = True
                        break
                    elif carga <= 60:
                        print("Estado del servidor actualizado.")
                        servidor["carga"] = carga
                        servidor["critico"] = False
                        break
            except ValueError:
                print("Debe ingresar un número decimal válido")
        else:
            print(f"No existe registro del servidor '{nombre}' en nuestra base de datos.")
    
#5. Función para mostrar lista de servidores
def mostrar_lista_servidores(servidores):
    if not servidores:
        print("¡No hay servidores registrados!")
    else:
        print("-- LISTA DE SERVIDORES REGISTRADOS EN EL SISTEMA --")
        print(f"Servidores encontrados: {len(servidores)}")
        for servidor in servidores:
            print("-"*45)
            print(f"Nombre: {servidor["nombre"]}")
            print(f"Uptime (Días): {servidor["uptime"]}")
            print(f"Uso del GPU (%): {servidor["carga"]}%")
            print(f"Estado crítico: {servidor["critico"]}")
            print("="*45)
#6. Función mensaje de salida
def mensaje_salida():
    import time
    print("Saliendo del programa... ")
    time.sleep(1)
    print("¡Adiós!")