def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def copias_genero(genero, dicc_libros, dicc_prestamos):
    genero_buscado = genero.strip().lower()
    total_copias = 0
    
    for codigo, datos in dicc_libros.items():
        if datos[2].strip().lower() == genero_buscado:
            if codigo in dicc_prestamos:
                total_copias += dicc_prestamos[codigo][1]
                
    print(f"El total de copias disponibles es: {total_copias}")

def busqueda_multa(multa_min, multa_max, dicc_libros, dicc_prestamos):
    resultados = []
    
    for codigo, datos_prestamo in dicc_prestamos.items():
        multa = datos_prestamo[0]
        copias = datos_prestamo[1]
        
        if multa_min <= multa <= multa_max and copias > 0:
            if codigo in dicc_libros:
                titulo = dicc_libros[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if resultados:
        resultados.sort()
        print(f"Los libros encontrados son: {resultados}")
    else:
        print("No hay libros en ese rango de multa.")

def agregar_libro(codigo, titulo, autor, genero, anio, editorial, es_novedad, precio_multa, copias_disponibles, dicc_libros, dicc_prestamos):
    cod_upper = codigo.upper()
    if cod_upper in dicc_libros:
        return False
        
    novedad_bool = True 
    if es_novedad.lower() == 's':
        es_novedad = True
    else:
        es_novedad = False
    
    dicc_libros[cod_upper] = [titulo, autor, genero, int(anio), editorial, novedad_bool]

def eliminar_libro(codigo, dicc_libros, dicc_prestamos):
    if buscar_codigo(codigo, dicc_prestamos):
        cod_upper = codigo.upper()
        del dicc_libros[cod_upper]
        del dicc_prestamos[cod_upper]
        return True
    return False