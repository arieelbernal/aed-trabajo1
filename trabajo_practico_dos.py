import random

# Sector Funciones


def generacion_carta():
    numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
    nombre_carta = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS")
    palo = ("Corazon", "Trebol", "Picas", "Diamante")
    x = random.randint(0, 12)
    y = random.randint(0, 3)
    carta_obtenida = (numero[x], nombre_carta[x], palo[y])
    return carta_obtenida

# Hay que arreglar en la validación un error en donde si el usuario selecciona la opción 1 (de apostar)
# e ingresa un número negativo, el pozo queda bien sin modificar, PERO, si el usuario vuelve a ingresar
# un monto positivo que puede ser útil, el pozo no se modifica.
# REVISAR INTERACCIÓN CON LÍNEA 227!!!!

def validacion(monto):
    if 100000 >= monto + pozo > 0 and monto > 0 and monto % 5 == 0:
        return monto
    else:
        # Acá (posiblemente) esté el error, en la bandera ok, que invalide el cambio. Revisar
        print("ERROR, el pozo no puede sobrepasar 100.000 ni \ntampoco podés apostar montos negativos.")
        ok = False
        return ok


def jugar_una_mano(pozo):
    hay_as = False
    hay_as_croupier = False
    acum_jugador_puntaje = 0
    acum_croupier_puntaje = 0
    cont_cartas_jugador = 0
    cont_cartas_croupier = 0
    i = 0

    #  print(apuesta_mano)
    # CARTAS JUGADOR
    print('*-' * 25)
    print("\t\tLas cartas del jugador son:")
    print()
    while i < 2:
        carta = (generacion_carta())
        print(carta)
        if i == 0:
            bandera_1er_carta_as(carta)
        if carta[0] == 11:
            hay_as = True
        acum_jugador_puntaje += carta[0]
        cont_cartas_jugador += 1
        i += 1
    # if acum_jugador_puntaje == 21 and (carta[0] == 11 and carta[1] == 10) or (carta[0] == 10 and carta[1] == 11):
    #     blackjack_natural = True
    print()
    print("La suma de las cartas del jugador hasta el momento \nes: ", acum_jugador_puntaje)
    print('*-' * 25)

    # PRIMERA CARTA CROUPIER
    print('*-' * 25)
    print("\t\tLa primera carta del croupier es: ")
    print()
    carta_croupier = (generacion_carta())
    print(carta_croupier)
    if carta_croupier[0] == 11:
        hay_as_croupier = True
    cont_cartas_croupier += 1
    acum_croupier_puntaje += (carta_croupier[0])
    print()
    print("\t\tLa suma de las cartas del croupier es: ", acum_croupier_puntaje)
    print('*-' * 25)

    # CARTAS JUGADOR
    print('*-' * 25)
    otra_carta = input("\t\tQuiere pedir otra carta?, s/n: ")
    print('*-' * 25)
    print()
    while acum_jugador_puntaje < 21 and otra_carta == "s":
        carta = generacion_carta()
        print(carta)
        if acum_jugador_puntaje > 21 and hay_as:
            acum_jugador_puntaje -= 10
            hay_as = False
        acum_jugador_puntaje += (carta[0])
        cont_cartas_jugador += 1
        print("La suma de las cartas del jugador hasta el momento \nes: ", acum_jugador_puntaje)
        print()
        print('*-' * 25)
        otra_carta = input("\t\tQuiere pedir otra carta?, s/n: ")
        print('*-' * 25)

    # CARTA CROUPIER
    while acum_croupier_puntaje < 17:
        print('*-' * 25)
        print("\t\tLa/las cartas del croupier son: ")
        print()
        carta_crupier = (generacion_carta())
        cont_cartas_croupier += 1
        if carta_crupier[0] == 11:
            hay_as_croupier = True
        print(carta_crupier)
        if acum_croupier_puntaje > 21 and hay_as_croupier:
            acum_croupier_puntaje -= 10
            hay_as_croupier = False
        acum_croupier_puntaje += (carta_crupier[0])
        # if acum_croupier_puntaje == 21 and (carta_crupier[0] == 11 and carta_crupier[1] == 10) or (carta_crupier[0] == 10 and carta_crupier[1] == 11):
        #     blackjack_natural = True
        print()
        print("La suma de las cartas del croupier hasta el momento \nes: ", acum_croupier_puntaje)
        print('*-' * 25)
        print("Valores de parametros", "puntaje jugador", acum_jugador_puntaje, "puntaje croupier",
              acum_croupier_puntaje, "Canntidad cartas jugador", cont_cartas_jugador, "Canntidad cartas croupier",
              cont_cartas_croupier, "Pozo", pozo)
    ganador, pozo, blackjack_natural = definir_ganador(acum_jugador_puntaje, acum_croupier_puntaje, cont_cartas_jugador,
                                                       cont_cartas_croupier, pozo)
    return ganador, pozo, blackjack_natural


def bandera_1er_carta_as(carta):
    if carta[0] == 11:
        return True
    return False


# Determinar ganador
def definir_ganador(puntaje_jugador, puntaje_croupier, cont_cartas_jugador, cont_cartas_croupier, pozo):
    ganador = None
    blackjack_nat = False
    if puntaje_jugador > 21 and puntaje_croupier > 21:
        ganador = "Croupier"
        pozo -= apuesta_mano
    elif puntaje_jugador == puntaje_croupier and puntaje_jugador < 21 and puntaje_croupier < 21:
        ganador = "¡Fue un empate!"
    elif puntaje_jugador == 21 and puntaje_croupier == 21:
        if cont_cartas_jugador == 2 and cont_cartas_croupier == 2:
            ganador = "¡Fue un empate!"
            blackjack_nat = True
            print("¡Ocurrió un Blackjack Natural! (Ás + una carta de valor 10.")
        elif cont_cartas_jugador != 2 and cont_cartas_croupier == 2:
            ganador = "Croupier"
            pozo -= apuesta_mano
        elif cont_cartas_jugador == 2 and cont_cartas_croupier != 2:
            ganador = "Jugador"
            pozo += apuesta_mano
    elif puntaje_jugador > 21:
        ganador = "Croupier"
        pozo -= apuesta_mano
    elif puntaje_croupier > 21:
        ganador = "Jugador"
        pozo += apuesta_mano
    elif puntaje_jugador > puntaje_croupier:
        ganador = "Jugador"
        pozo += apuesta_mano
        if cont_cartas_jugador == 2 and puntaje_jugador == 21:
            print("¡El jugador obtuvo un Blackjack Natural!")
            blackjack_nat = True
    elif cont_cartas_croupier == 2 and puntaje_croupier == 21:
        ganador = "Croupier"
        print("¡El croupier obtuvo un Blackjack Natural!")
        blackjack_nat = True
        pozo -= apuesta_mano
    elif (cont_cartas_jugador == 2 and puntaje_jugador == 21) and (cont_cartas_croupier == 2 and puntaje_croupier == 21):
        ganador = "¡Fue un empate!"
    else:
        ganador = "Croupier"
        pozo -= apuesta_mano
    if ganador == "¡Fue un empate!":
        print("No hay ganador, ¡EMPATARON!")
    else:
        print("El ganador es: ", ganador)
    print("Su pozo actual es:", pozo)
    return ganador, pozo, blackjack_nat


def mayor(primer_valor, segundo_valor):
    if primer_valor > segundo_valor:
        return primer_valor
    return segundo_valor
# Fin sector de funciones


# Sector Principal
print('*-' * 25)
bandera_nombre_valido = True
nombre_jugador = input("\t¡Hola! Por favor, ingrese su nombre: ")
if nombre_jugador == "" or nombre_jugador == " ":
    bandera_nombre_valido = False
pozo = 0
opcion = None
contador_jugadas = 0
contador_ganadas_jugador = 0
racha_croupier = 0
mayor_racha_croupier = 0
pozo_maximo = 0
acumulador_apuestas_jugador = 0
mayor_perdida = 0
cont_black_natural = 0
bandera_usuario_ingreso_numero_correcto = True
bandera_carga_pozo_inicial = True

while bandera_carga_pozo_inicial is True:
    print('*-' * 25)
    print("Para comenzar a jugar, no ingrese números negativos,\n ni un número mayor o igual que 100.000")
    print('*-' * 25)
    pozo = int(input("Ingrese el monto inicial del pozo, con valores \nentre 0 y 100.000: "))
    if pozo < 0 or pozo > 100000:
        print("ERROR. Usted ha ingresado un número NO VÁLIDO. \n")
        print("Se le ha pedido un monto que NO sea negativo \n o que no sea superior a 100.000 pesos.")
        print("Será enviad@ de vuelta a la pantalla de carga \ndel pozo inicial.")
        bandera_usuario_ingreso_numero_correcto = False
        continue
    else:
        if 0 <= pozo <= 100000:
            bandera_usuario_ingreso_numero_correcto = True
            print("El valor inicial del pozo es de: ", pozo, "pesos.")
            bandera_carga_pozo_inicial = False

pozo_maximo = mayor(pozo, pozo_maximo)

while opcion != "0" and (bandera_usuario_ingreso_numero_correcto is True) and bandera_nombre_valido is True:
    print('*-' * 25)
    print("¡Bienvenid@ al Blackjack! Estimad@", nombre_jugador, "\n¿Desea probar su suerte? ¿O se irá sin guita?")
    print('*-' * 25)
    print()
    print('*-' * 25)
    print("\t1) APOSTAR (AUMENTE EL POZO) \n\t2) JUEGUE UNA MANO (APUESTE Y BUENA SUERTE) \n\t0) SALIR Y MOSTRAR LOS "
          "RESULTADOS")
    print('*-' * 25)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        suma_de_pozo = int(input("Ingrese el dinero a aumentar de su pozo: "))
        if validacion(suma_de_pozo):
            suma_de_pozo_validada = validacion(suma_de_pozo)
            pozo += suma_de_pozo_validada
            pozo_maximo = mayor(pozo, pozo_maximo)
        print("El valor del pozo actual es de :", pozo, "pesos.")

    elif opcion == "2":
        print('*-' * 25)
        apuesta_mano = int(input("Ingrese la apuesta para esta mano: "))
        print("El pozo actual es de: ", pozo, " pesos.")
        print('*-' * 25)
        if validacion(apuesta_mano) <= pozo:
            acumulador_apuestas_jugador += apuesta_mano
            ganador_jugada, pozo, blackjack_natural = jugar_una_mano(pozo)
            if ganador_jugada == "Jugador":
                racha_croupier = 0
                contador_ganadas_jugador += 1
            elif ganador_jugada == "Croupier":
                racha_croupier += 1
                mayor_perdida = mayor(mayor_perdida, apuesta_mano)
                mayor_racha_croupier = mayor(mayor_racha_croupier, racha_croupier)
            contador_jugadas += 1
            pozo_maximo = mayor(pozo, pozo_maximo)
            if blackjack_natural:
                cont_black_natural += 1
        else:
            print("No posee fondos suficientes. Intente realizando una apuesta más baja.")
            print('*-' * 25)

    elif opcion == "0":
        print('*-' * 25)
        print(f'{nombre_jugador} esperamos que haya disfrutado su juego')
        print('*-' * 25)


# Arreglar salidas ya que no tienen un display correcto de los valores que deberían ser

print('*-' * 25)
print("RESULTADOS DE LA PARTIDA: ")
print()
print(f'La racha mas larga del croupier fue de {mayor_racha_croupier} partidas ganadas.')
print(f'Porcentaje de victorias del jugador {contador_ganadas_jugador*100/contador_jugadas}%.')
print(f'Mayor pozo que tuvo el jugador: {pozo_maximo}.')
print(f'Valor promedio de apuestas por jugada: {acumulador_apuestas_jugador/contador_jugadas} pesos.')
print(f'La mayor perdida del jugador es: {mayor_perdida} pesos.')
print(f'El pozo actual es: {pozo} pesos.')
print(f'Cantidad de rondas donde hubo Blackjack Nartural: {cont_black_natural}.')
print()
print('*-' * 25)
