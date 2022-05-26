import random

def generacion_carta():
    numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
    nombre_carta = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS")
    palo = ("Corazon", "Trebol", "Picas", "Diamante")
    x = random.randint(0, 12)
    y = random.randint(0, 3)
    carta_obtenida = (numero[x], nombre_carta[x], palo[y])
    carta_mismo_numero = (numero[x], palo[y])

    if str(numero[x]) == nombre[x]:
        return carta_mismo_numero
    else:
        return carta_obtenida


def validacion(monto):
    if 100000 >= monto + pozo > 0 and monto != 0 and monto % 5 == 0:
        return monto
    return 0


def jugar_una_mano():
    acum_jugador = 0
    acum_croupier = 0
    i = 0
    hay_AS =
    print("Las cartas del jugador son:")
    while i < 2:
        carta = (generacion_carta())
        print(carta)
        acum_jugador += carta[0]

        i += 1
    print("La suma de las cartas del jugador hasta el momento es: ", acum_jugador)

    print("La primera carta del crupier es: ")
    carta_crupier = (generacion_carta())
    print(carta_crupier)
    acum_croupier += (carta_crupier[0])
    print("La suma de las cartas del crupier es: ", acum_croupier)

    otra_carta = input("Quiere pedir otra carta?, s/n: ")
    while otra_carta != "n" or otra_carta != "N" and acum_jugador < 21:
        carta = (generacion_carta())
        print(carta)
        acum_jugador += (carta[0])
        otra_carta = input("Quiere pedir otra carta?, s/n: ")





def definir_ganador(puntaje_jugador, puntaje_croupier):
    if(puntaje_croupier):
    return None

nombre = input("Ingrese su nombre: ")
pozo = 0
opcion = None


while pozo <= 0 or pozo > 100000:
    valor = int(input("Ingrese el monto inicial del pozo: "))
    pozo += validacion(valor)

while opcion != "0":
    print("1)Apostar\n2)Jugar una mano\n0)Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        valor = int(input("Ingrese el monto para sumar al pozo: "))
        pozo += validacion(valor)
    elif opcion == "2":
        apuesta_mano = int(input("Ingrese la apuesta para esta mano: "))
        if validacion(apuesta_mano) <= pozo:
            jugar_una_mano()
        else:
            print("No posee fondos suficientes.")
    elif opcion == "0":
        print(f'{nombre} esperamos que haya disfrutado su juego')
jugar_una_mano()
