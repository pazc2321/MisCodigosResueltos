"""
Esta es mi versión simplificada de Monopoly.
Está adaptada por mi para ser una forma rápida y jugable en una terminal como esta!
Es una adaptación de las reglas oficiales de juego rápido de Monopoly.
(¿¿¿Oda al capitalismo???)

    -- REGLAS Y CARACTERÍSTICAS --
    1. ¡COMENZAMOS!
        - Monto inicial:
        Cada jugador comienza con $1000

        - Reparto inicial:
        El banquero reparte 2 cartas de Título de Propiedad a cada jugador,
        quienes deben pagar inmediatamente al banco el valor total de 
        estas propiedades.

        - Renta
        Si caes en una propiedad con dueño, deberás pagarle la renta. Esta es la
        mitad del costo de la propiedad.

    2 . Salida
    Cada vez que un jugador pasa por la salida cobra $250.

    3. La carcel
    Para salir de la cárcel tienes dos opciones: 
        - Sacas dobles al primer intento.
        - Pagas $50.

    4. El ganador
    Gana quien tenga más efectivo en su cuenta. El dinero se contabiliza tanto de
    la billetera como de las propiedades.

    5. El juego acaba cuando:
        - El primer jugador quede en bancarrota (ó)
        - Se acaben los turnos
    
    -- INCLUYE --
    Tablero(12 Casillas en total)
    0: Salida
    1: Avenida Mediterráneo
    2: Impuestos
    3: Avenida Oriental
    4: Avenida San Carlos
    5: Avenida Tennessee
    6: Cárcel
    7: Avenida Illinois
    8: Fortuna
    9: Avenida Ventnor
    10: Avenida Pensilvania
    11: El Muelle

        Títulos de Propiedad(8)
        GRUPO CAFÉ                  Valor Propiedad     Renta
            Avenida Mediterráneo - - - - $60 - - - - -  $30
        GRUPO CELESTE
            Avenida Oriental - - - - - - $100 - - - - - $50
        GRUPO ROSA
            Avenida San Carlos - - - - - $140 - - - - - $70
        GRUPO NARANJA
            Avenida Tennessee - - - - -  $180 - - - - - $90
        GRUPO ROJO
            Avenida Illinois - - - - - - $240 - - - - - $120
        GRUPO AMARILLO
            Avenida Venthor - - - - - -  $260 - - - - - $130
        GRUPO VERDE
            Avenida Pensilvania - - - -  $320 - - - - - $160
        GRUPO AZUL
            El Muelle - - - - - - - - -  $400 - - - - - $200
    
        Dados(2)
        Fichas(2)
"""
#Importar
import time
import random
import subprocess
import os

#Inicializar
casillasTablero = 12
pasos = 0
numTurno = 1


#Fichas
def arte_ficha(ficha):
    if ficha == "perro":
        print(r""",'.-.'. 
'\~ o/` ,,
{ @ } f
/`-'\$ 
(_/-\_)""")
    else:
        print(r""" ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-""")
         
#Dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    pasos = dado1 + dado2
    print(f"Lanzaste los dados: ⚁ [{dado1}] y ⚄ [{dado2}] -> ¡Avanzas {pasos} casillas!")
    return pasos

def limpiar():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

#Jugadores: Dentro de diccionarios.
jugador_1 = {
    "billetera": 1000,
    #"propiedades": Se agregará al comprar la primera propiedad
    "ficha": "perro",
    "posicion": 0,
    "en_carcel": False
    
}

jugador_maquina = {
    "billetera": 1000,
    #"propiedades": Se agregará al comprar la primera propiedad
    "ficha": "auto",
    "posicion": 0,
    "en_carcel": False
}

#Casillas
#0 Salida
casilla_0 = {
    "nombre": "Salida",
    "valor_p": 0,
    "renta": 0,
    "dueno": "Banco"
}

#1: Avenida Mediterráneo
casilla_1 = {
    "nombre": "Avenida Mediterráneo",
    "valor_p": 60,
    "renta": 30,
    "dueno": None
}

#2: Impuestos
casilla_2 = {
    "nombre": "Impuestos",
    "valor_p": 0,
    "renta": 0,
    "dueno": "Banco"
}

#3: Avenida Oriental
casilla_3 = {
    "nombre": "Avenida Oriental",
    "valor_p": 100,
    "renta": 50,
    "dueno": None
}
      
#4: Avenida San Carlos
casilla_4 = {
    "nombre": "Avenida San Carlos",
    "valor_p": 140,
    "renta": 70,
    "dueno": None
}    

#5: Avenida Tennessee
casilla_5 = {
    "nombre": "Avenida Tennessee",
    "valor_p": 180,
    "renta": 90,
    "dueno": None
}

#6: Cárcel
casilla_6 = {
    "nombre": "Cárcel",
    "valor_p": 0,
    "renta": 0,
    "dueno": "Banco"
}

#7: Avenida Illinois
casilla_7 = {
    "nombre": "Avenida Illinois",
    "valor_p": 240,
    "renta": 120,
    "dueno": None
}

#8: Fortuna
casilla_8 = {
    "nombre": "Fortuna",
    "valor_p": 0,
    "renta": 0,
    "dueno": "Banco"
}

#9: Avenida Ventnor
casilla_9 = {
    "nombre": "Avenida Ventnor",
    "valor_p": 260,
    "renta": 130,
    "dueno": None
}

#10: Avenida Pensilvania
casilla_10 = {
    "nombre": "Avenida Pensilvania",
    "valor_p": 320,
    "renta": 160,
    "dueno": None
}

#11: El Muelle
casilla_11 = {
    "nombre": "El Muelle",
    "valor_p": 400,
    "renta": 200,
    "dueno": None
}

#Tablero: Una gran lista
tablero = [casilla_0, casilla_1, casilla_2, casilla_3, 
           casilla_4, casilla_5, casilla_6, casilla_7,
           casilla_8, casilla_9, casilla_10, casilla_11]

#---  C O M I E N Z A  E L  J U E G O  ---
#Reparto inicial (código)
propiedades_libres = [casilla_1, casilla_3, casilla_4, casilla_5, 
                      casilla_7, casilla_9, casilla_10, casilla_11]

prop_random = random.sample(propiedades_libres, 2)

print("--- ¡Bienvenido a MONOPOLY ---")
print("[1]: Perro\n[2]: Auto")

#Elegir una ficha
while True:
    try:
        ficha = input("Elige tu ficha, escribiendo su nombre: ").lower()
        if ficha != "perro" and ficha != "auto":
            raise ValueError
    except ValueError:
        print("Opción no válida")
    
    if ficha == "perro":
        print("...")
        time.sleep(1)
        jugador_1["ficha"] = ficha
        jugador_maquina["ficha"] = "auto"
        print("¡Ficha seleccionada!")
        break
    elif ficha == "auto":
        print("...")
        time.sleep(1)
        jugador_1["ficha"] = ficha
        jugador_maquina["ficha"] = "perro"
        print("¡Ficha seleccionada!")
        break

#Reparto inicial
print(f"## ¡ES TURNO DE '{jugador_1['ficha']}'! ##")
arte_ficha(jugador_1["ficha"])

print(f"Billetera: ${jugador_1["billetera"]}")
time.sleep(1)
print("El banco está varajando las propiedades ...")
time.sleep(3)
print("Eligiendo...\n")
propiedades = random.sample(propiedades_libres, 2)

for propiedad in propiedades:
    print(f"- ¡Eres dueño de '{propiedad["nombre"]}'!")

    jugador_1["billetera"] -= propiedad["valor_p"]
    propiedad["dueno"] = "jugador_1"
    
print(f"Billetera: ${jugador_1['billetera']}\n")

time.sleep(2)
print(f"## ¡ES TURNO DE '{jugador_maquina['ficha']}'! ##")
arte_ficha(jugador_maquina["ficha"])

print(f"Billetera: ${jugador_maquina["billetera"]}")
time.sleep(1)
print("El banco está varajando las propiedades ...")
time.sleep(3)
print("Eligiendo...\n")
propiedades_restantes = [p for p in propiedades_libres if p["dueno"] is None]
propiedades = random.sample(propiedades_restantes, 2)

for propiedad in propiedades:
    print(f"- ¡{jugador_maquina['ficha']} es dueño de '{propiedad["nombre"]}'!")

    jugador_maquina["billetera"] -= propiedad["valor_p"]
    propiedad["dueno"] = "jugador_maquina"

print(f"Billetera: ${jugador_1['billetera']}\n")

#-- S E  L A N Z A N  L O S  D A D O S --
#Bucle de los turnos
while True:
    input("Presiona ENTER para lanzar los dados ⚁⚄")
    limpiar()
    pasos = lanzar_dados()

    jugador_1["posicion"] += pasos

    if jugador_1["posicion"] >= casillasTablero:
        jugador_1["posicion"] -= 12 #(casilla 0)
        jugador_1["billetera"] += 250 #Dinero al pasar por la salida
        print("¡Pasaste por la salida! Cobraste $250")

    casilla_actual = tablero[jugador_1["posicion"]]
    print(f"Caiste {casilla_actual["nombre"]}\n")
    time.sleep(1)

    #Acciones para la casilla:

    #TURNO MAQUINA
    print(f"'{jugador_maquina["ficha"]}' está lanzando los dados...")
    time.sleep(1)
    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    pasos = dado1 + dado2

    jugador_maquina["posicion"] =+ pasos

    if jugador_maquina["posicion"] > casillasTablero:
        jugador_maquina["posicion"] -= 12 #(casilla 0)
        jugador_maquina["billetera"] += 250 #Dinero al pasar por la salida
        print("¡Pasó por la salida y cobró $250")

    casilla_actual = tablero[jugador_maquina["posicion"]]
    print(f"{jugador_maquina["ficha"]} cayó en {casilla_actual["nombre"]}")

    numTurno += 1

    if numTurno == 3:
        break




