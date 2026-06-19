import validaciones as vld
def main():
    coleccion_servidores = []
    while True:
        vld.mostrar_opciones()
        opcion = vld.solicitar_opcion()
        if opcion == 1:
            vld.registrar_servidor(coleccion_servidores)
        elif opcion == 2:
            busqueda = input("Ingrese el nombre del servidor a buscar: ")
            posicion = vld.localizar_servidor(coleccion_servidores, busqueda)
            if posicion != -1:
                serv =  coleccion_servidores[posicion]
                print(f"\n[Servidor encontrado en índice: {posicion}]")
                print(f"Nombre: {serv}['nombre']")
                print(f"Uptime: {serv}['uptime'] días")
                print(f"Carga: {serv}['carga'] %")
                print(f"Estado Crítico: {'Si' if serv['critico'] else 'NO'}")
            else:
                print(f"El servidor '{busqueda}' no se encuentra registrado")
        elif opcion == 3:
            eliminar = input("Ingrese el nombre del servidor a eliminar: ")
            posicion = vld.localizar_servidor(coleccion_servidores, eliminar)
            if posicion != -1:
                coleccion_servidores.pop(posicion)
                print("El servidor ha sido eliminado del sistema")
            else:
                print(f"El servidor {eliminar} no se encuentra registrado")
        elif opcion == 4:
            vld.procesar_alertas(coleccion_servidores)
        elif opcion == 5:
            vld.procesar_alertas(coleccion_servidores)
            print("\n === LISTA DE SERVIDORES ===")
            for serv in coleccion_servidores:
                texto_estado = "CRITICO" if serv["critico"] else "estable"
                print(f"Nombre: {serv}['nombre']")
                print(f"Uptime: {serv}['uptime'] días")
                print(f"Carga: {serv}['carga'] %")
                print(f"Estado Crítico: {texto_estado}")
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente con un número del 1 al 6")

if __name__ == "__main__":
    main()