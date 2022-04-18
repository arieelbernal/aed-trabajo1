"""
    Trabajo práctico número 1 del grupo TP1-G051
"""

import random

print('*' * 60)
print("           Trabajo Práctico #1 Grupo TP1-G051  ")
print()
print("                       Integrantes: ")
print()
print("     Berzero, Virginia Maria; Legajo: 96631; Comisión: 1K06 ")
print("    Jiménez, Melani Milagros; Legajo: 94443; Comisión: 1K06 ")
print("       Murúa, Martina; Legajo: 94644; Comisión: 1K06 ")
print("Rodriguez Bernal, Ariel Hernán; Legajo: 89985; Comisión: 1K06 ")
print(" Romero Moreno, Oscar Alfonso; Legajo: 96454; Comisión: 1K06 ")
print('*' * 60)

# Datos
# Constantes
PUNTAJE_MAXIMO = 21
LIMITE_TERCERA_JUGADA = 17
# Fin de la carga de Constantes

# Nombre del jugador, reglas del juego.
print()
print('*' * 60)
jugador = input("  ¡Bienvenido al Blackjack! Por favor ingrese su nombre: ")
print('*' * 60)
print('                    REGLAS DEL JUEGO')
print('*' * 60)
print("En este juego estimad@", jugador, "para ganar necesitas conseguir\n "
      "un puntaje superior al de nuestro croupier ""y además, \n menor o igual a 21.")
print()
print("Se disputarán 3 tiradas, en las que en la primera y se \n"
      "mostrarán si ambas cartas son del mismo palo y del\n "
      "mismo valor si ambas resultan ser del mismo palo.")
print()
print("Se mostrará al final de cada turno el puntaje parcial\n "
      "obtenido de cada tirada y al final se mostrará\n el "
      "puntaje total.")
print()
print("En caso de que te excedas de los 21 puntos, o tengas menos\n"
      "puntos que el croupier, habrás perdido el juego.")
print()
print("Si ustedes dos tienen el mismo puntaje o llegan a tener \n"
      "ambos 21, habrán terminado en un empate.")
print()
print('*' * 60)
print('             ¿CUÁNTOS PUNTOS VALE CADA CARTA?')
print('*' * 60)
print('- \'As\' = El Ás vale 11 si el puntaje es menor a 11 y vale 1\n'
      'cuando el puntaje es mayor o igual a 11.')
print('- \'Jack (J)\', \'Queen (Q)\' o \'King (K)\' = Las tres cartas \n'
      'valen 10 puntos respectivamente cada una.')
print('- Cartas de Valor Numérico = Tendrán el mismo valor que el\n'
      'número que indica la misma carta.')
print()
print('*' * 60)
print('                 ¿ESTÁS LIST@ PARA JUGAR?')
print('*' * 60)
print(input("Presiona la tecla \"Enter\" para empezar a jugar."))

# Inicialización de variables del juego
puntaje_jugador = 0
puntaje_croupier = 0
cartas = ("As (A)", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack (J)", "Queen (Q)", "King (K)")
palos = ("Picas", "Corazones", "Diamantes", "Tréboles")
primera_carta = ("", "")
primera_carta_igual_palo = False
misma_primera_carta = False
bandera_de_aparicion_de_figuras = False

# Mensajes personalizados - Victoria
mensajes_aleatorios_victoria = ("¡¡¡Wauuuu!!! ¡Has ganado! ¡Una canción pa' \
celebrar!: https://youtu.be/JVv08IZVMEg", "¡Increíiible! ¡Ganasteeee! \
¿Jugamos otra?", "¿¡Cómooo?! ¡¿Ganaste!? ¡Hiciste trampaaa! \
¡Quiero la revancha!", "¡Imposible! Tenemos a alguien que hackeo \
nuestro programa... y ganó...", "¡Has ganado 1 MILLÓN DE PESOSSS! Naaa, \
¡te la creíste! Sólo somos estudiantes.")

# Mensajes personalizados - Derrota
mensajes_aleatorios_derrota = ("¡¡¡Has perdido!!! Pobrecit@, mira, ¡ten aquí \
un premio de consolación!: https://youtu.be/dQw4w9WgXcQ", "¡¡Noooo!! ¡Te ganó\
 el croupier!¡¿Cómo puede ser?!", "¡Perdiste! ¡Ten 50 pesos para que te \
 compres una Manaos!", "Jijiji... ¡Parece que alguien perdióoo! ¿Lo \
 intentas de nuevo?", "¿Quién perdióoo? ¡Túuuu! ¡Vamos a jugar otra \
 vez!")

# Primera tirada del jugador.
print('*' * 60)
print('          ¡PRIMERA TIRADA! ¡QUE COMIENCE EL JUEGO!')
print('*' * 60)
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "As (A)":
    puntaje_jugador += 11
else:
    if carta_al_azar_jugador[0] == "Jack (J)" or \
            carta_al_azar_jugador[0] == "Queen (Q)" or \
            carta_al_azar_jugador[0] == "King (K)":
        puntaje_jugador += 10
        bandera_de_aparicion_de_figuras = True
    else:
        puntaje_jugador += carta_al_azar_jugador[0]

print("La carta del jugador es:", carta_al_azar_jugador[0], "de", carta_al_azar_jugador[1])
print(jugador, "tu puntaje en la primera tirada es:", puntaje_jugador)

# Primera tirada del croupier.
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "As (A)":
    puntaje_croupier += 11
else:
    if carta_al_azar_croupier[0] == "Jack (J)" or \
            carta_al_azar_croupier[0] == "Queen (Q)" or \
            carta_al_azar_croupier[0] == "King (K)":
        puntaje_croupier += 10
        bandera_de_aparicion_de_figuras = True
    else:
        puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del croupier es:", carta_al_azar_croupier[0], "de",
      carta_al_azar_croupier[1])
print("El puntaje del croupier en la primera tirada es:",
      puntaje_croupier)

# Puntos 3.) y 4.) del TP - Comparativa de las cartas de la primera tirada:
# Si ambos comparten el mismo palo en la primera tirada...
if carta_al_azar_jugador[1] == carta_al_azar_croupier[1]:
    primera_carta_igual_palo = True
    # Si ambos son también el mismo número en la primera tirada...
    if carta_al_azar_jugador[0] == carta_al_azar_croupier[0]:
        misma_primera_carta = True
        primera_carta = carta_al_azar_jugador

# Comparativa puntos jugador vs. croupier primera tirada.
if puntaje_jugador > puntaje_croupier:
    print('*' * 60)
    print("            ¡ Enhorabuena, vas ganando", jugador, "!")
    print('*' * 60)
else:
    if puntaje_jugador < puntaje_croupier:
        print('*' * 60)
        print("            ¡Noooo! ¡Vas perdiendo por ahora...!")
        print('*' * 60)
    else:
        print('*' * 60)
        print("¡Vaya vaya! ¡Estamos empatados en la primera tirada!")
        print('*' * 60)
# Fin de comparativa primera tirada

print('*' * 60)
print(input("Presiona la tecla \"Enter\" para jugar la segunda tirada."))

# Inicio Segunda Tirada
# Segunda tirada del jugador
print('*' * 60)
print('               ¡SEGUNDA TIRADA! ¡VAMOOOOOS!')
print('*' * 60)
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "As (A)":
    if puntaje_jugador < 11:
        puntaje_jugador += 11
    else:
        if puntaje_jugador >= 11:
            puntaje_jugador += 1
else:
    if carta_al_azar_jugador[0] == "Jack (J)" or \
            carta_al_azar_jugador[0] == "Queen (Q)" or \
            carta_al_azar_jugador[0] == "King (K)":
        puntaje_jugador += 10
        bandera_de_aparicion_de_figuras = True
    else:
        puntaje_jugador += carta_al_azar_jugador[0]

print("La carta del jugador es:", carta_al_azar_jugador[0], "de",
      carta_al_azar_jugador[1])
print(jugador, "tu puntaje en la segunda tirada es:", puntaje_jugador)
# Segunda tirada del croupier.
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "As (A)":
    if puntaje_croupier < 11:
        puntaje_croupier += 11
    else:
        puntaje_croupier += 1
else:
    if carta_al_azar_croupier[0] == "Jack (J)" or \
            carta_al_azar_croupier[0] == "Queen (Q)" or \
            carta_al_azar_croupier[0] == "King (K)":
        puntaje_croupier += 10
        bandera_de_aparicion_de_figuras = True
    else:
        puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del croupier es:", carta_al_azar_croupier[0], "de",
      carta_al_azar_croupier[1])
print("El puntaje del croupier en la segunda tirada es:", puntaje_croupier)

# Comparativa puntos jugador vs. croupier segunda tirada.
if puntaje_croupier < puntaje_jugador < 21 and puntaje_croupier < PUNTAJE_MAXIMO:
    print('*' * 60)
    print("                 ¡Muy bien", jugador, "!")
    print('*' * 60)
if puntaje_jugador < puntaje_croupier < PUNTAJE_MAXIMO and \
        puntaje_jugador < PUNTAJE_MAXIMO:
    print('*' * 60)
    print("                       ¡Que mal!")
    print('*' * 60)
if puntaje_jugador == puntaje_croupier and puntaje_croupier < 21 and \
        puntaje_jugador < 21:
    print('*' * 60)
    print("                      ¡¿Empatad@s?!")
    print('*' * 60)
# Fin comparativa segunda tirada.

# Tercera tirada del jugador (opcional si el puntaje es menor a 17).
if puntaje_jugador < LIMITE_TERCERA_JUGADA or \
        puntaje_croupier < LIMITE_TERCERA_JUGADA:
    print(input("Presiona la tecla \"Enter\" para jugar la tercera tirada."))
    print('*' * 60)
    print('               ¡TERCERA TIRADA! ¡LA GRAN FINAL!')
    print('*' * 60)
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if puntaje_jugador < LIMITE_TERCERA_JUGADA:
    if carta_al_azar_jugador[0] == "As (A)":
        if puntaje_jugador < 11:
            puntaje_jugador += 11
        else:
            puntaje_jugador += 1
    else:
        if carta_al_azar_jugador[0] == "Jack (J)" or \
                carta_al_azar_jugador[0] == "Queen (Q)" or \
                carta_al_azar_jugador[0] == "King (K)":
            puntaje_jugador += 10
            bandera_de_aparicion_de_figuras = True
        else:
            puntaje_jugador += carta_al_azar_jugador[0]

    print("La carta del jugador es:", carta_al_azar_jugador[0], "de",
          carta_al_azar_jugador[1])

print(jugador, "tu puntaje en la tercera tirada es:", puntaje_jugador)

# Tercera tirada del croupier (opcional si el puntaje es menor o igual a 16).
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if puntaje_croupier < LIMITE_TERCERA_JUGADA:
    if carta_al_azar_croupier[0] == "As (A)":
        if puntaje_croupier < 11:
            puntaje_croupier += 11
        else:
            puntaje_croupier += 1
    else:
        if carta_al_azar_croupier[0] == "Jack (J)" or \
                carta_al_azar_croupier[0] == "Queen (Q)" or \
                carta_al_azar_croupier[0] == "King (K)":
            puntaje_croupier += 10
            bandera_de_aparicion_de_figuras = True
        else:
            puntaje_croupier += carta_al_azar_croupier[0]
    print("La carta del croupier es:", carta_al_azar_croupier[0], "de",
          carta_al_azar_croupier[1])
print("El puntaje del croupier en la tercera tirada es:", puntaje_croupier)

# Condiciones de victoria, derrota o empate por puntuación:
if puntaje_croupier == puntaje_jugador <= 21 or \
        (puntaje_jugador > PUNTAJE_MAXIMO and
         puntaje_croupier > PUNTAJE_MAXIMO):
    print('*' * 60)
    print("        ¡NINGUNO GANA ESTA VEZ!")
else:
    if (puntaje_croupier < puntaje_jugador <= 21) or \
            puntaje_croupier > PUNTAJE_MAXIMO:
        print('*' * 60)
        print("                          ¡GANASTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_victoria))
    else:
        print('*' * 60)
        print("                          ¡PERDISTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_derrota))

# Print de analisis de la primera carta
if primera_carta_igual_palo:
    print('*' * 60)
    print("La primera carta tanto para el jugador como para \
el croupier fue del mismo palo")
    if misma_primera_carta:
        print("No solo eso, fue la misma carta:", primera_carta[0], "de",
              primera_carta[1])
# Bandera de figuras en la partida:
if bandera_de_aparicion_de_figuras:
    print('*' * 60)
    print("En esta partida aparecio alguna de estas cartas: Jack (J), Queen \
(Q) o King (K)")
    print('*' * 60)
