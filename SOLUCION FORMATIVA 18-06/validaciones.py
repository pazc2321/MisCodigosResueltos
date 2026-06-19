def mostrar_opciones():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar servidor")
    print("2. Buscar servidor") 
    print("3. Eliminar servidor")
    print("4. Actualizar estados")
    print("5. Mostrar servidores") 
    print("6. Salir")

def solicitar_opcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        return opcion
    except ValueError:
        return -1

#VALIDACIONES
def validar_nombre(nombre):
    return len(nombre.strip()) > 0 #ni en blanco ni espacios en blanco
def validar_uptime(uptime_str):
    try:
        valor = int(uptime_str)
        return valor > 0
    except ValueError:
        return False
def validar_carga(carga_str):
    try:
        valor = float(carga_str)
        return 1.0 <= valor <= 100.0
    except ValueError:
        return False
def registrar_servidor(lista_servidor):
    print("\ Registrar Servidor")
    nom = input("Ingrese nombre del servidor: ")
    upt = input("Ingrese días de uptime: ")
    crg = input("Ingrese porcentaje de carga de CPU (1.0 - 100.0): ")
    if not validar_nombre(nom):
        print("Error: El nombre no puede estar vacío")
        return
    if not validar_uptime(upt):
        print("Error: El uptime debe ser un número entero mayor a 0")
        return
    if not validar_carga(crg):
        print("Error: La carga debe ser un número decimal entre 1.0 y 100.0")
        return
    #SI PASA LAS VALIDACIONES, SE CREA EL DICCIONARIO:
    nuevo_servidor = {
        "nombre": nom.strip(),
        "uptime": int(upt),
        "carga": float(crg),
        "critico": False
    }
    lista_servidor.append(nuevo_servidor)
    print("Servidor registrado exitosamente.")

def localizar_servidor(lista_servidor, nombre_abuscar):
    for i in range(len(lista_servidor)):
        if lista_servidor[i]["nombre"].lower() == nombre_abuscar.lower():
            return i
        return -1
def procesar_alertas(lista_servidor):
    for servidor in lista_servidor:
        if servidor["carga"] >= 75.0:
            servidor["critico"] =  True
        else:
            servidor["critico"] = False