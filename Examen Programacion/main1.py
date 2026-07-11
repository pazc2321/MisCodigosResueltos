import funciones1 as funciones

def main():
    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
    }

    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Copias por género")
        print("2. Búsqueda de libros por rango de multa")
        print("3. Actualizar multa de libro")
        print("4. Agregar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        print("=====================================")
        
        opcion = funciones.leer_opcion()
        
        if opcion == 1:
            gen = input("Ingrese género a consultar: ")
            funciones.copias_genero(gen, libros, prestamos)
            
        elif opcion == 2:
            while True:
                try:
                    m_min = int(input("Ingrese multa mínima: "))
                    m_max = int(input("Ingrese multa máxima: "))
                    if m_min >= 0 and m_max >= 0 and m_min <= m_max:
                        funciones.busqueda_multa(m_min, m_max, libros, prestamos)
                        break
                    else:
                        print("Las multas deben ser >= 0 y la mínima menor o igual a la máxima.")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            pass       
        elif opcion == 4:
            cod = input("Ingrese código del libro: ")
            if not funciones.validar_codigo(cod, libros):
                print("Error: Código inválido o ya existente.")
                continue
                
            tit = input("Ingrese título: ")
            if not funciones.validar_texto(tit):
                print("Error: Título inválido.")
                continue
                
            aut = input("Ingrese autor: ")
            if not funciones.validar_texto(aut):
                print("Error: Autor inválido.")
                continue
                
            gen = input("Ingrese género: ")
            if not funciones.validar_texto(gen):
                print("Error: Género inválido.")
                continue
                
            a_str = input("Ingrese año de publicación: ")
            if not funciones.validar_anio(a_str):
                print("Error: Año inválido.")
                continue
                
            edit = input("Ingrese editorial: ")
            if not funciones.validar_texto(edit):
                print("Error: Editorial inválida.")
                continue
                
            nov_str = input("¿Es novedad? (s/n): ")
            if not funciones.validar_novedad(nov_str):
                print("Error: Opción inválida para novedad.")
                continue
                
            m_str = input("Ingrese precio de multa: ")
            if not funciones.validar_multa(m_str):
                print("Error: Precio de multa inválido.")
                continue
                
            cop_str = input("Ingrese copias disponibles: ")
            if not funciones.validar_copias(cop_str):
                print("Error: Copias disponibles inválidas.")
                continue
            
            if funciones.agregar_libro(cod, tit, aut, gen, a_str, edit, nov_str, m_str, cop_str, libros, prestamos):
                print("Libro agregado")
            else:
                print("El código ya existe")
                
        elif opcion == 5:
            cod = input("Ingrese código del libro que desea eliminar: ")
            if funciones.eliminar_libro(cod, libros, prestamos):
                print("Libro eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()