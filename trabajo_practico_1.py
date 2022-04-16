"""
    Trabajo práctico número 1 del grupo TP1-G051
"""

import random

# Datos
cartas = ("Ás (A)", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Comodín (J)", "Reina (Q)", "Rey (K)")
palos = ("Picas", "Corazones", "Diamantes", "Tréboles")
salio_figura = False
PUNTAJE_MAXIMO = 21
# jugador = input("Ingresa tu nombre: ")
jugador = input("¡Bienvenido al Blackjack! Por favor ingrese su nombre: ")
puntaje_jugador = 0
puntaje_croupier = 0
mismo_palo = False
cartas_iguales= ("", "")

# Procedimientos
# Primer tirada del jugador
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "Ás (A)":
    puntaje_jugador += 11
else:
    if cartas.index(carta_al_azar_jugador[0]) > 9:
        puntaje_jugador += 10
        salio_figura = True
    else:
        puntaje_jugador += carta_al_azar_jugador[0]
print("Tu carta es:", carta_al_azar_jugador[0], "de",
      carta_al_azar_jugador[1])
print(jugador, "tu puntaje es:", puntaje_jugador)

# Primera tirada del croupier
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "Ás (A)":
    puntaje_croupier += 11
else:
    if cartas.index(carta_al_azar_croupier[0]) > 9:
        puntaje_croupier += 10
        salio_figura = True
        print("¡Ha salido la figura", random.randrange(carta_al_azar_jugador[0]), "en la primera tirada del croupier!")
    else:
        puntaje_croupier += carta_al_azar_croupier[0]
print("La carta del croupier es", carta_al_azar_croupier[0], "de",
      carta_al_azar_croupier[1])
print("El puntaje del croupier es:", puntaje_croupier)

# Comparación de la primera tirada
if carta_al_azar_jugador[1] == carta_al_azar_croupier[1]:
    mismo_palo = True
    if carta_al_azar_jugador[0] == carta_al_azar_croupier[0]:
        cartas_iguales = carta_al_azar_jugador

# Segunda tirada jugador
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "Ás (A)":
    if puntaje_jugador + 11 <= PUNTAJE_MAXIMO:
        puntaje_jugador += 11
    else:
        puntaje_jugador += 1
else:
    if cartas.index(carta_al_azar_jugador[0]) > 9:
        puntaje_jugador += 10
        salio_figura = True
    else:
        puntaje_jugador += carta_al_azar_jugador[0]
print("Tu carta es:", carta_al_azar_jugador[0], "de",
      carta_al_azar_jugador[1])
print(jugador, "tu puntaje es:", puntaje_jugador)

# Segunda tirada croupier
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "Ás (A)":
    if puntaje_croupier + 11 <= PUNTAJE_MAXIMO:
        puntaje_croupier += 11
    else:
        puntaje_croupier += 1
else:
    if cartas.index(carta_al_azar_croupier[0]) > 9:
        puntaje_croupier += 10
        salio_figura = True
    else:
        puntaje_croupier += carta_al_azar_croupier[0]
print("La carta del croupier es", carta_al_azar_croupier[0], "de",
      carta_al_azar_croupier[1])
print("El puntaje del croupier es:", puntaje_croupier)

# Tercera tirada del jugador
carta_al_azar_jugador = (random.choice(cartas), random.choice(palos))
if carta_al_azar_jugador[0] == "Ás (A)":
    if puntaje_jugador + 11 <= PUNTAJE_MAXIMO:
        puntaje_jugador += 11
        print("Tu carta es:", carta_al_azar_jugador[0], "de",
              carta_al_azar_jugador[1])
    else:
        if puntaje_jugador + 1 <= PUNTAJE_MAXIMO:
            puntaje_jugador += 1
            print("Tu carta es:", carta_al_azar_jugador[0], "de",
                  carta_al_azar_jugador[1])
else:
    if cartas.index(carta_al_azar_jugador[0]) > 9:
        if puntaje_jugador + 10 <= PUNTAJE_MAXIMO:
            puntaje_jugador += 10
            salio_figura = True
            print("Tu carta es:", carta_al_azar_jugador[0], "de",
                  carta_al_azar_jugador[1])
    else:
        if puntaje_jugador + carta_al_azar_jugador[0] <= PUNTAJE_MAXIMO:
            puntaje_jugador += carta_al_azar_jugador[0]
            print("Tu carta es:", carta_al_azar_jugador[0], "de",
                  carta_al_azar_jugador[1])

# Tercera tirada del croupier
carta_al_azar_croupier = (random.choice(cartas), random.choice(palos))
if carta_al_azar_croupier[0] == "Ás (A)":
    if puntaje_croupier + 11 <= PUNTAJE_MAXIMO:
        puntaje_croupier += 11
        print("La carta del croupier es", carta_al_azar_croupier[0], "de",
              carta_al_azar_croupier[1])
    else:
        if puntaje_croupier + 1 <= PUNTAJE_MAXIMO:
            puntaje_croupier += 1
            print("La carta del croupier es", carta_al_azar_croupier[0], "de",
                  carta_al_azar_croupier[1])
else:
    if cartas.index(carta_al_azar_croupier[0]) > 9:
        if puntaje_croupier + 10 <= PUNTAJE_MAXIMO:
            puntaje_croupier += 10
            salio_figura = True
            print("La carta del croupier es", carta_al_azar_croupier[0], "de",
                  carta_al_azar_croupier[1])
    else:
        if puntaje_croupier + carta_al_azar_croupier[0] <= PUNTAJE_MAXIMO:
            puntaje_croupier += carta_al_azar_croupier[0]
            print("La carta del croupier es", carta_al_azar_croupier[0], "de",
                  carta_al_azar_croupier[1])

# Comparación de puntajes y resultados
if puntaje_jugador > puntaje_croupier:
    print(jugador, "ha ganado la partida con", puntaje_jugador, "puntos")
else:
    print("El croupier ha ganado esta partida con", puntaje_croupier,
          "puntos, suerte para la próxima")
if mismo_palo:
    print("Las cartas de la primera tirada fueron del mismo palo")
    if cartas_iguales != ("", ""):
        print("Tanto a", jugador, "como al croupier les salio:",
              cartas_iguales[0], "de", cartas_iguales[1],
              "en su primera tirada")
if salio_figura:
    print("En alguna tirada apareció una figura")
