import random

# Sector Inicialización


# Sector Funciones


def generacion_carta():
    numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
    nombre_carta = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS")
    palo = ("Corazon", "Trebol", "Picas", "Diamante")
    x = random.randint(0, 12)
    y = random.randint(0, 3)
    carta_obtenida = (numero[x], nombre_carta[x], palo[y])
#    carta_mismo_numero = (numero[x], palo[y])
    return carta_obtenida
#   if str(numero[x]) == nombre[x]:
#       return carta_mismo_numero
#   else:
#       return carta_obtenida


def validacion(monto):
    if 100000 >= monto + pozo > 0 and monto > 0 and monto % 5 == 0:
        return monto
    else:
        print("ERROR, el pozo no puede sobrepasar 100.000")
        ok = False
        return ok


def jugar_una_mano(pozo):
    hay_AS = False
    hay_AS_croupier = False
    blackjack_natural = False
    acum_jugador_puntaje = 0
    acum_croupier_puntaje = 0
    cont_cartas_jugador = 0
    cont_cartas_croupier = 0
    i = 0

    print(apuesta_mano)
    #CARTAS JUGADOR
    print("Las cartas del jugador son:")
    while i < 2:
        carta = (generacion_carta())
        print(carta)
        if i == 0:
            bandera_1er_carta_AS(carta)
        if carta[0] == 11:
            hay_AS = True
        acum_jugador_puntaje += carta[0]
        cont_cartas_jugador += 1
        i += 1
    print("La suma de las cartas del jugador hasta el momento es: ", acum_jugador_puntaje)
    if acum_jugador_puntaje == 21:
        blackjack_natural = True

    #PRIMERA CARTA CROUPIER
    print("La primera carta del crupier es: ")
    carta_croupier = (generacion_carta())
    print(carta_croupier)
    if carta_croupier[0] == 11:
        hay_AS_croupier = True
    cont_cartas_croupier += 1
    acum_croupier_puntaje += (carta_croupier[0])
    print("La suma de las cartas del crupier es: ", acum_croupier_puntaje)

    #CARTAS JUGADOR
    otra_carta = input("Quiere pedir otra carta?, s/n: ")
    while acum_jugador_puntaje < 21 and otra_carta == "s":
        carta = generacion_carta()
        print(carta)
        if acum_jugador_puntaje > 21 and hay_AS:
            acum_jugador_puntaje -= 10
            hay_AS = False
        acum_jugador_puntaje += (carta[0])
        cont_cartas_jugador += 1
        print("La suma de las cartas del jugador hasta el momento es: ", acum_jugador_puntaje)
        otra_carta = input("Quiere pedir otra carta?, s/n: ")





    #CARTA CRUPIER
    while acum_croupier_puntaje < 17:
        print("La/las cartas del croupier son: ")
        carta_crupier = (generacion_carta())
        cont_cartas_croupier += 1
        if carta_crupier[0] == 11:
            hay_AS_croupier = True
        print(carta_crupier)
        if acum_croupier_puntaje > 21 and hay_AS_croupier:
            acum_croupier_puntaje -= 10
            hay_AS_croupier = False
        acum_croupier_puntaje += (carta_crupier[0])
        print("La suma de las cartas del crupier hasta el momento es: ", acum_croupier_puntaje)
    ganador, pozo = definir_ganador(acum_jugador_puntaje, acum_croupier_puntaje, cont_cartas_jugador, cont_cartas_croupier, pozo)
    return ganador, pozo, blackjack_natural




def bandera_1er_carta_AS(carta):
    if carta[0] == 11:
        return True
    return False


# Determinar ganador
def definir_ganador(puntaje_jugador, puntaje_croupier,cont_cartas_jugador, cont_cartas_croupier, pozo):
    ganador = None
    if puntaje_jugador > 21 and puntaje_croupier > 21:
        ganador = "croupier"
        pozo -= apuesta_mano
    elif puntaje_jugador == puntaje_croupier and puntaje_jugador <= 21 and puntaje_croupier <= 21:
        ganador = "empate"
    elif puntaje_jugador == 21 and puntaje_croupier == 21:
        if cont_cartas_jugador == 2 and cont_cartas_croupier == 2:
            ganador = "empate"
    elif cont_cartas_jugador != 2 and cont_cartas_croupier == 2:
        ganador = "croupier"
        pozo -= apuesta_mano
    elif cont_cartas_croupier != 2 and cont_cartas_jugador == 2:
        ganador = "jugador"
        pozo += apuesta_mano
    elif puntaje_jugador > 21:
        ganador = "croupier"
        pozo -= apuesta_mano
    elif puntaje_croupier > 21:
        ganador = "jugador"
        pozo += apuesta_mano
    elif puntaje_jugador > puntaje_croupier:
        ganador = "jugador"
        pozo += apuesta_mano
    else:
        ganador = "croupier"
        pozo -= apuesta_mano
    if ganador == "empate":
        print("No hay ganador, ¡EMPATARON!")
    else:
        print("El ganador es: ", ganador)
    print("Su pozo actual es:", pozo)
    return ganador, pozo


def mayor(primer_valor, segundo_valor):
    if primer_valor > segundo_valor:
        return primer_valor
    return segundo_valor


# Fin Sector Funciones

# Sector Principal
nombre_jugador = input("Ingrese su nombre: ")
pozo = 0
opcion = None
contador_jugadas = 0
contador_ganadas_jugador = 0
racha_croupier = 0
racha_mas_larga = 0
pozo_maximo = 0
acumulador_apuestas_jugador = 0
mayor_perdida = 0
cont_black_natural = 0

while pozo <= 0 or pozo > 100000:
    pozo = int(input("Ingrese el monto inicial del pozo, con valores entre 0 y 100.000: "))

pozo_maximo = mayor(pozo, pozo_maximo)

while opcion != "0":
    print("1)Apostar\n2)Jugar una mano\n0)Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        suma_de_pozo = int(input("Ingrese el dinero a aumentar de su pozo: "))
        if validacion(suma_de_pozo):
            suma_de_pozo_validada = validacion(suma_de_pozo)
            pozo += suma_de_pozo_validada
            pozo_maximo = mayor(pozo, pozo_maximo)
        print("El pozo actual es:", pozo)

    elif opcion == "2":
        print("El pozo actual es: ", pozo)
        apuesta_mano = int(input("Ingrese la apuesta para esta mano: "))
        if validacion(apuesta_mano) <= pozo:
            acumulador_apuestas_jugador += apuesta_mano
            ganador_jugada, pozo, blackjack_natural = jugar_una_mano(pozo)
            if ganador_jugada == "jugador":
                racha_croupier = 0
                contador_ganadas_jugador += 1
            elif ganador_jugada == "croupier":
                racha_croupier += 1
                mayor_perdida = mayor(mayor_perdida, apuesta_mano)
            contador_jugadas += 1
            pozo_maximo = mayor(pozo, pozo_maximo)
            if blackjack_natural:
                cont_black_natural += 1
        else:
            print("No posee fondos suficientes.")

    elif opcion == "0":
        print(f'{nombre_jugador} esperamos que haya disfrutado su juego')


print(f'La racha mas larga del croupier fue {mayor(racha_mas_larga, racha_croupier)}')
print(f'Porcentaje de victorias del jugador {contador_ganadas_jugador*100/contador_jugadas}')
print(f'Mayor pozo que tuvo el jugador {pozo_maximo}')
print(f'Valor promedio de apuestas por jugada {acumulador_apuestas_jugador/contador_jugadas}')
print(f'La mayor perdida del jugador es {mayor_perdida}')
print(f'El pozo actual es: {pozo}')
print(f'Cantidad de rondas donde hubo Blackjack Nartural: {cont_black_natural}')
