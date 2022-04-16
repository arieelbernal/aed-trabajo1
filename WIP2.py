"""
    Trabajo práctico número 1 del grupo TP1-G051
"""

import random


print('*' * 60)
print("          \U0001F642 Trabajo Práctico #1 Grupo TP1-G051 \U0001F609 ")
print()
print("                       Integrantes: ")
print()
print("     Berzero, Virginia Maria; Legajo: 96631; Comisión: 1K06 ")
print("    Jiménez, Melani Milagros; Legajo: 94443; Comisión: 1K06 ")
print("       Murúa, Martina; Legajo: 94644; Comisión: 1K06 ")
print("Rodriguez Bernal, Ariel Hernán; Legajo: 89985; Comisión: 1K06 ")
print(" Romero Moreno, Oscar Alfonso; Legajo: 96454; Comisión: 1K06 ")
print('*' * 60)


# Agregar interactividad haciendo que el usuario apriete un botón o clic para hacer que sea un juego.
# Mostrar puntaje parcial después de cada tirada.

# Datos
# Constantes
PUNTAJE_MAXIMO = 21
PUNTAJE_PARA_TERCERA_CARTA = 16

# Fin de la carga de Constantes

# Carga de Variables

# Nombre del jugador, reglas del juego.
print()
print('*' * 60)
jugador = input("  ¡Bienvenido al Blackjack! Por favor ingrese su nombre: ")
print('*' * 60)
print('                    REGLAS DEL JUEGO')
print('*' * 60)
print("En este juego estimad@", jugador, "para ganar necesitas conseguir\n un puntaje superior al de nuestro croupier "
                                         "y además, \n menor o igual a 21.")
print()
print("Se disputarán 3 tiradas, en las que en la primera y se \n"
      "mostrarán si ambas cartas son del mismo palo y del\n "
      "mismo valor si ambas resultan ser del mismo palo.")
print()
print("Se mostrará al final de cada turno el puntaje parcial\n obtenido de cada tirada y al final se mostrará\n el "
      "puntaje total.")
print()
print("En caso de que te excedas de los 21 puntos, o tengas menos \npuntos que el croupier, habrás perdido el juego.")
print()
print("Si ustedes dos tienen el mismo puntaje o llegan a tener \nambos 21, habrán terminado en un empate.")
print()
print('*' * 60)
print('             ¿CUÁNTOS PUNTOS VALE CADA CARTA?')
print('*' * 60)
print('- \'Ás\' = El Ás vale 11 si el puntaje es menor a 11 y vale 1 \ncuando el puntaje es mayor o igual a 11.')
print('- \'Comodín (J)\', \'Reina (Q)\' o \'Rey (K)\' = Las tres cartas \n'
      'valen 10 puntos respectivamente cada una.')
print('- Cartas de Valor Numérico = Tendrán el mismo valor que el \nnúmero que indica la misma carta.')
print()
print('*' * 60)
print('                 ¿ESTÁS LIST@ PARA JUGAR?')
print('*' * 60)
print(input("Presiona la tecla \"Enter\" para empezar a jugar."))

# Inicialización de puntajes tanto para el jugador como para el croupier (servirán de acumulación).
puntaje_jugador = 0
puntaje_croupier = 0
# Fin de la carga de Variables

#  Procesos
# Determinación de palos, cartas y tuplas tanto del jugador como del croupier.
cartas = ("Ás (A)", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Comodín (J)", "Reina (Q)", "Rey (K)")
palos = ("Picas", "Corazones", "Diamantes", "Tréboles")
carta_al_azar_jugador = (random.choice(cartas), "de", random.choice(palos))
carta_al_azar_croupier = (random.choice(cartas), "de", random.choice(palos))
bandera_de_aparicion_de_figuras = 0
jugador_gano = False
if puntaje_jugador <= 21 and puntaje_jugador > 16:
    jugador_gano = True
croupier_gano = False
if puntaje_croupier <= 21 and puntaje_croupier > 16:
    croupier_gano = True

# Mensajes personalizados - Victoria
mensajes_aleatorios_victoria = ("¡¡¡Wauuuu!!! ¡Has ganado! ¡Una canción pa' celebrar!: \
https://youtu.be/JVv08IZVMEg", "\
¡Increíiible! ¡Ganasteeee! ¿Jugamos otra?", "\
¿¡Cómooo?! ¡¿Ganaste!? ¡Hiciste trampaaa! ¡Quiero la revancha!", "\
¡Imposible! Tenemos a alguien que hackeo nuestro programa... y ganó...", "\
¡Has ganado 1 MILLÓN DE PESOSSS! Naaa, ¡te la creíste! Sólo somos estudiantes.")

# Mensajes personalizados - Derrota
mensajes_aleatorios_derrota = ("¡¡¡Has perdido!!! Pobrecit@, mira, ¡ten aquí un premio de '\
'consolación!: \
https://youtu.be/dQw4w9WgXcQ", "\
¡¡Noooo!! ¡Te ganó el croupier! ¡¿Cómo puede ser?!",
"¡Perdiste! ¡Ten 50 pesos para que te compres una Manaos!",
"Jijiji... ¡Parece que alguien perdióoo! ¿Lo intentas de nuevo?",
"¿Quién perdióoo? ¡Túuuu! ¡Vamos a jugar otra vez!")


# Primera tirada del jugador.
print('*' * 60)
print('          ¡PRIMERA TIRADA! ¡QUE COMIENCE EL JUEGO!')
print('*' * 60)
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "Ás (A)":
    puntaje_jugador += 11
else:
    if carta_al_azar_jugador[0] == "Comodín (J)":
        puntaje_jugador += 10
        print('¡Apareció la figura: Comodín (J) en la mano del jugador!')
        bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
    else:
        if carta_al_azar_jugador[0] == "Reina (Q)":
            puntaje_jugador += 10
            print('¡Apareció la figura: Reina (Q) en la mano del jugador!')
            bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_jugador[0] == "Rey (K)":
                puntaje_jugador += 10
                print('¡Apareció la figura: Rey (K) en la mano del jugador!')
                bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                puntaje_jugador += carta_al_azar_jugador[0]

print("La carta del jugador es:", carta_al_azar_jugador[0], "de", carta_al_azar_jugador[1])
print(jugador, "tu puntaje en la primera tirada es:", puntaje_jugador)

# Primera tirada del croupier.
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "Ás (A)":
    puntaje_croupier += 11
else:
    if carta_al_azar_croupier[0] == "Comodín (J)":
        puntaje_croupier += 10
        print('¡Apareció la figura: Comodín (J) en la mano del croupier!')
        bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
    else:
        if carta_al_azar_croupier[0] == "Reina (Q)":
            puntaje_croupier += 10
            print('¡Apareció la figura: Reina (Q) en la mano del croupier!')
            bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_croupier[0] == "Rey (K)":
                puntaje_croupier += 10
                print('¡Apareció la figura: Rey (K) en la mano del croupier!')
                bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del croupier es:", carta_al_azar_croupier[0], "de", carta_al_azar_croupier[1])
print("El puntaje del croupier en la primera tirada es:", puntaje_croupier)

# Puntos 3.) y 4.) del TP - Comparativa de las cartas de la primera tirada:
# Si ambos comparten el mismo palo en la primera tirada...
if carta_al_azar_jugador[1] == carta_al_azar_croupier[1]:
    print("¡La primera carta del jugador y del croupier es del mismo palo!")

# Si ambos son tanto del mismo palo como el mismo número en la primera tirada...
if carta_al_azar_jugador[1] == carta_al_azar_croupier[1] and carta_al_azar_jugador[0] == carta_al_azar_croupier[0]:
    print("¡Además de ser del mismo palo, ambas cartas son del mismo valor!")

# Comparativa puntos jugador vs. croupier primera tirada.
if puntaje_jugador > puntaje_croupier:
    print('*' * 60)
    print("            ¡ Enhorabuena, vas ganando", jugador,"!")
    print('*' * 60)
if puntaje_croupier > puntaje_jugador:
    print('*' * 60)
    print("            ¡Noooo! ¡Vas perdiendo por ahora...!")
    print('*' * 60)
if puntaje_jugador == puntaje_croupier:
    print('*' * 60)
    print("¡Vaya vaya! ¡Estamos empatados en la primera tirada!")
    print('*' * 60)

'''
# Fin Comparativa
print(input("Presiona la tecla \"Enter\" para jugar la segunda tirada."))
# Fin Primera Tirada
'''

# Inicio Segunda Tirada
# Segunda tirada del jugador
print('*' * 60)
print('               ¡SEGUNDA TIRADA! ¡VAMOOOOOS!')
print('*' * 60)
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "Ás (A)":
    if puntaje_jugador < 11:
        puntaje_jugador += 11
    else:
        if puntaje_jugador >= 11:
            puntaje_jugador += 1
else:
    if carta_al_azar_jugador[0] == "Comodín (J)":
        puntaje_jugador += 10
        print('¡Apareció la figura: Comodín (J) en la mano del jugador!')
        bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
    else:
        if carta_al_azar_jugador[0] == "Reina (Q)":
            puntaje_jugador += 10
            print('¡Apareció la figura: Reina (Q) en la mano del jugador!')
            bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_jugador[0] == "Rey (K)":
                puntaje_jugador += 10
                print('¡Apareció la figura: Rey (K) en la mano del jugador!')
                bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                puntaje_jugador += carta_al_azar_jugador[0]

print("La carta del jugador es:", carta_al_azar_jugador[0], "de", carta_al_azar_jugador[1])
print(jugador, "tu puntaje en la segunda tirada es:", puntaje_jugador)

if puntaje_jugador == PUNTAJE_MAXIMO:
    print('*' * 60)
    print("                    ¡GANASTE! ¡BLACKJACK! LET'S GOOO!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_victoria))
    jugador_gano = True
else:
    if puntaje_jugador > PUNTAJE_PARA_TERCERA_CARTA:
        print('*' * 60)
        print("                        ¡GANASTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_victoria))
        jugador_gano = True

# Segunda tirada del croupier.
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if jugador_gano == False:
    if carta_al_azar_croupier[0] == "Ás (A)":
        if puntaje_croupier < 11:
           puntaje_croupier += 11
    else:
        if puntaje_croupier >= 11:
            puntaje_croupier += 1
else:
    if jugador_gano == False:
        if carta_al_azar_croupier[0] == "Comodín (J)":
           puntaje_croupier += 10
           print('¡Apareció la figura: Comodín (J) en la mano del croupier!')
           bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_croupier[0] == "Reina (Q)":
               puntaje_croupier += 10
               print('¡Apareció la figura: Reina (Q) en la mano del croupier!')
               bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                if carta_al_azar_croupier[0] == "Rey (K)":
                   puntaje_croupier += 10
                   print('¡Apareció la figura: Rey (K) en la mano del croupier!')
                   bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
                else:
                    puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del croupier es:", carta_al_azar_croupier[0], "de", carta_al_azar_croupier[1])
print("El puntaje del croupier en la segunda tirada es:", puntaje_croupier)

if puntaje_croupier == PUNTAJE_MAXIMO:
    print('*' * 60)
    print("            ¡PERDISTE! ¡BLACKJACK DEL CROUPIER!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_derrota))
    croupier_gano = True
else:
    if puntaje_croupier > PUNTAJE_PARA_TERCERA_CARTA:
        print('*' * 60)
        print("                          ¡PERDISTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_derrota))
        croupier_gano = True

# Comparativa puntos jugador vs. croupier segunda tirada.
if puntaje_jugador > puntaje_croupier and puntaje_croupier < 21 and puntaje_jugador < 21:
    print('*' * 60)
    print("                 ¡Muy bien", jugador,"!")
    print('*' * 60)
if puntaje_croupier > puntaje_jugador and puntaje_croupier < 21 and puntaje_jugador < 21:
    print('*' * 60)
    print("                       ¡Que mal!")
    print('*' * 60)
if puntaje_jugador == puntaje_croupier and puntaje_croupier < 21 and puntaje_jugador < 21:
    print('*' * 60)
    print("                      ¡¿Empatad@s?!")
    print('*' * 60)
# Fin Comparativa

# Fin de la segunda tirada.
'''
if puntaje_jugador <= PUNTAJE_PARA_TERCERA_CARTA and puntaje_croupier <= PUNTAJE_PARA_TERCERA_CARTA and \
        croupier_gano == False and jugador_gano == False:
    print(input("Presiona la tecla \"Enter\" para jugar la tercera tirada."))
'''
# Inicio Tercera Tirada
# Tercera tirada del jugador (opcional si el puntaje es menor o igual a 16).
print('*' * 60)
print('               ¡TERCERA TIRADA! ¡LA GRAN FINAL!')
print('*' * 60)
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if croupier_gano == False and jugador_gano == False:
    if carta_al_azar_croupier[0] == "Ás (A)":
        if puntaje_croupier < 11:
           puntaje_croupier += 11
    else:
        if puntaje_croupier >= 11:
            puntaje_croupier += 1
else:
    if croupier_gano == False and jugador_gano == False:
        if carta_al_azar_croupier[0] == "Comodín (J)":
           puntaje_croupier += 10
           print('¡Apareció la figura: Comodín (J) en la mano del croupier!')
           bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_croupier[0] == "Reina (Q)":
               puntaje_croupier += 10
               print('¡Apareció la figura: Reina (Q) en la mano del croupier!')
               bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                if carta_al_azar_croupier[0] == "Rey (K)":
                   puntaje_croupier += 10
                   print('¡Apareció la figura: Rey (K) en la mano del croupier!')
                   bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
                else:
                    puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del jugador es:", carta_al_azar_jugador[0], "de", carta_al_azar_jugador[1])
print(jugador, "tu puntaje en la tercera tirada es:", puntaje_jugador)

# Tercera tirada del croupier (opcional si el puntaje es menor o igual a 16).
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if jugador_gano == False and croupier_gano == False:
    if carta_al_azar_croupier[0] == "Ás (A)":
        if puntaje_croupier < 11:
           puntaje_croupier += 11
    else:
        if puntaje_croupier >= 11:
            puntaje_croupier += 1
else:
    if jugador_gano == False and croupier_gano == False:
        if carta_al_azar_croupier[0] == "Comodín (J)":
           puntaje_croupier += 10
           print('¡Apareció la figura: Comodín (J) en la mano del croupier!')
           bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
        else:
            if carta_al_azar_croupier[0] == "Reina (Q)":
               puntaje_croupier += 10
               print('¡Apareció la figura: Reina (Q) en la mano del croupier!')
               bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
            else:
                if carta_al_azar_croupier[0] == "Rey (K)":
                   puntaje_croupier += 10
                   print('¡Apareció la figura: Rey (K) en la mano del croupier!')
                   bandera_de_aparicion_de_figuras = bandera_de_aparicion_de_figuras + 1
                else:
                    puntaje_croupier += carta_al_azar_croupier[0]

print("La carta del jugador es:", carta_al_azar_croupier[0], "de", carta_al_azar_croupier[1])
print("El puntaje del croupier en la tercera tirada es:", puntaje_croupier)

# Condiciones de victoria, derrota o empate por puntuación:
# Victoria del jugador si es Blackjack (llega al 21) o si tiene más puntos que el croupier:
if puntaje_jugador == PUNTAJE_MAXIMO:
    print('*' * 60)
    print("              ¡GANASTE! ¡BLACKJACK! LET'S GOOO!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_victoria))
    jugador_gano = True
else:
    if puntaje_jugador > puntaje_croupier:
        print('*' * 60)
        print("                        ¡GANASTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_victoria))
        jugador_gano = True

# Victoria del jugador si el croupier se pasa de 21 puntos:
if puntaje_croupier > 21 and puntaje_jugador <= 21:
    print('*' * 60)
    print("        ¡EL CROUPIER SE PASÓ DE LOS 21 PUNTOS! ¡GANASTE!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_derrota))
    jugador_gano = True

# Derrota
if puntaje_croupier == PUNTAJE_MAXIMO:
    print('*' * 60)
    print("            ¡PERDISTE! ¡BLACKJACK DEL CROUPIER!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_derrota))
    croupier_gano = True

else:
    if puntaje_croupier > puntaje_jugador:
        print('*' * 60)
        print("                          ¡PERDISTE!")
        print('*' * 60)
        print(random.choice(mensajes_aleatorios_derrota))
        croupier_gano = True


# Derrota jugador por pasarse de 21 puntos:
if puntaje_jugador > 21 and puntaje_croupier <= 21:
    print('*' * 60)
    print("       ¡TE FUISTE VOLANDO POR LAS NUBES! ¡PERDISTE!")
    print('*' * 60)
    print(random.choice(mensajes_aleatorios_derrota))
    croupier_gano = True

# Empate:
if puntaje_jugador > 21 and puntaje_croupier > 21:
    print('*' * 60)
    print("        ¡ES UN EMPATEEEEEEEEEEEE! ¡A JUGAR DE NUEVO!")
    print('*' * 60)

if puntaje_jugador == puntaje_croupier:
    print('*' * 60)
    print("        ¡ES UN EMPATEEEEEEEEEEEE! ¡A JUGAR DE NUEVO!")
    print('*' * 60)

# Cantidad de figuras que aparecieron en toda la partida:
print('*' * 60)
print("La cantidad de figuras que aparecieron en la partida fue de:", bandera_de_aparicion_de_figuras, ".")
print('*' * 60)
