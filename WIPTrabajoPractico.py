"""
    Trabajo práctico número 1 del grupo TP1-G051
"""

import random

# Agregar interactividad haciendo que el usuario apriete un botón o clic para hacer que sea un juego.
# Mostrar puntaje parcial después de cada tirada.

# Datos
# Constantes
PUNTAJE_MAXIMO = 21

# Fin de la carga de Constantes
palos_jugador = ('Espadas', 'Corazones', 'Diamantes', 'Tréboles')
palos_croupier = ('Espadas', 'Corazones', 'Diamantes', 'Tréboles')
J, Q, K = 'Comodín (J)', 'Reina (Q)', 'Rey (K)'  # Inicializamos variables para las cadenas de texto.
tupla_de_solo_figuras = J, Q, K  # Estas cadenas de texto devolverán el nombre de las figuras.
lista_de_figuras = 'Comodín (J)', 'Reina (Q)', 'Rey (K)'
A = 'Ás'
tupla_de_valores_numericos = 2, 3, 4, 5, 6, 7, 8, 9, 10  # Primera Tupla a concatenar
tupla_de_figuras_y_ases = J, Q, K, A  # Segunda Tupla a concatenar
tupla_de_todo = tupla_de_valores_numericos, tupla_de_figuras_y_ases  # Tupla de 2 Dimensiones

# Datos - Inicializando los puntajes para cada persona
# Puntos jugador
puntos_jugador_iniciales = 0
puntos_jugador_primera_tirada = 0
puntos_jugador_segunda_tirada = 0
puntos_jugador_tercera_tirada = 0
puntos_jugador_primera_tirada += puntos_jugador_iniciales
puntos_jugador_segunda_tirada += puntos_jugador_primera_tirada
puntos_jugador_tercera_tirada += puntos_jugador_segunda_tirada

# Puntos croupier
puntos_croupier_iniciales = 0
puntos_croupier_primera_tirada = 0
puntos_croupier_segunda_tirada = 0
puntos_croupier_tercera_tirada = 0
puntos_croupier_primera_tirada += puntos_jugador_iniciales
puntos_croupier_segunda_tirada += puntos_jugador_primera_tirada
puntos_croupier_tercera_tirada += puntos_jugador_segunda_tirada

# Procesos - Lógica de la Selección de cartas del jugador
# Se hará random choice, del random choice, para que con la tupla de dos dimensiones que armamos, podamos
# seleccionar por azar primero una de las 2 tuplas: o la tupla de los números del 1 al 10, o la tupla de las figuras
# y del Ás, de esa forma podremos evaluar que si por azar el sistema seleccionó la tupla de las figuras y del Ás,
# si el valor coincide con el número 10, según su posición, se le asignará que es o una carta Joker (J),
# una Queen (Q), o una King (K) y se mosatrará en pantalla (SÓLO se mostrarán que son figuras, aquellos '10s',
# # que pertenezcan a la tupla de tupla_de_figuras_y_ases.

# Primera Tirada
print('*'*45)
print("¡Primera tirada de la mano! ¡¿Quién ganará!?")
print('*'*45)
print()

# Generador de Palos de Cartas al Azar

palo_aleatorio_jugador_primera_tirada = random.choice(palos_jugador)
palo_aleatorio_croupier_primera_tirada = random.choice(palos_croupier)
palo_aleatorio_jugador_segunda_tirada = random.choice(palos_jugador)
palo_aleatorio_croupier_segunda_tirada = random.choice(palos_croupier)
palo_aleatorio_jugador_tercera_tirada = random.choice(palos_jugador)
palo_aleatorio_croupier_tercera_tirada = random.choice(palos_croupier)

# Fin del Generador


# Selección de Cartas al Azar Primera Tirada
valor_aleatorio_jugador_primer_turno = random.choice(random.choice(tupla_de_todo))
print('La primera carta del jugador es: ', valor_aleatorio_jugador_primer_turno, 'de',
      palo_aleatorio_jugador_primera_tirada)
valor_aleatorio_croupier_primer_turno = random.choice(random.choice(tupla_de_todo))
print('La primera carta del croupier es: ', valor_aleatorio_croupier_primer_turno, 'de',
      palo_aleatorio_croupier_primera_tirada)
# Fin Selección de Cartas al Azar

# Mostrar la aparición de una Figura, según como aparezca en la segunda tupla, usando condicional:
# Inicio Figuras Jugador:
if valor_aleatorio_jugador_primer_turno == tupla_de_figuras_y_ases[0]:
    print('¡Apareció la figura: Comodín (J) en la mano del jugador!')
    puntos_jugador_primera_tirada += 10
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')
elif valor_aleatorio_jugador_primer_turno == tupla_de_figuras_y_ases[1]:
    print('¡Apareció la figura: Reina (Q) en la mano del jugador!')
    puntos_jugador_primera_tirada += 10
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')
elif valor_aleatorio_jugador_primer_turno == tupla_de_figuras_y_ases[2]:
    print('¡Apareció la figura: Rey (K) en la mano del jugador!')
    puntos_jugador_primera_tirada += 10
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')
elif valor_aleatorio_jugador_primer_turno == tupla_de_figuras_y_ases[3]:
    print('¡Es un Ás!')
    puntos_jugador_primera_tirada += 11
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')
else:
    puntos_jugador_primera_tirada += valor_aleatorio_jugador_primer_turno
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')

# Fin Figuras Jugador:
# Inicio Figuras Croupier:
if valor_aleatorio_croupier_primer_turno == tupla_de_figuras_y_ases[0]:
    print('¡Apareció la figura: Comodín (J) en la mano del croupier!')
    puntos_croupier_primera_tirada += 10
    print('¡Hasta ahora, los puntos del croupier son:', puntos_croupier_primera_tirada, 'puntos!')
elif valor_aleatorio_croupier_primer_turno == tupla_de_figuras_y_ases[1]:
    print('¡Apareció la figura: Reina (Q) en la mano del croupier!')
    puntos_croupier_primera_tirada += 10
    print('¡Hasta ahora, los puntos del croupier son:', puntos_croupier_primera_tirada, 'puntos!')
elif valor_aleatorio_croupier_primer_turno == tupla_de_figuras_y_ases[2]:
    print('¡Apareció la figura: Rey (K) en la mano del croupier!')
    puntos_croupier_primera_tirada += 10
    print('¡Hasta ahora, los puntos del croupier son:', puntos_croupier_primera_tirada, 'puntos!')
elif valor_aleatorio_jugador_primer_turno == tupla_de_figuras_y_ases[3]:
    print('¡Es un Ás!')
    puntos_croupier_primera_tirada += 11
    print('¡Hasta ahora, los puntos del jugador son:', puntos_jugador_primera_tirada, 'puntos!')
else:
    puntos_croupier_primera_tirada += valor_aleatorio_croupier_primer_turno
    print('¡Hasta ahora, los puntos del croupier son:', puntos_croupier_primera_tirada, 'puntos!')
# Fin Figuras Croupier:

# Puntos 3.) y 4.) del TP - Comparativa de las cartas de la primera tirada:
# Si ambos comparten el mismo palo en la primera tirada...
if palo_aleatorio_jugador_primera_tirada == palo_aleatorio_croupier_primera_tirada:
   print("¡La primera carta del jugador y del crupier es del mismo palo!")

# Si ambos son tanto del mismo palo como el mismo número en la primera tirada...
if palo_aleatorio_jugador_primera_tirada == palo_aleatorio_croupier_primera_tirada and valor_aleatorio_jugador_primer_turno == valor_aleatorio_croupier_primer_turno:
   print("¡Además de ser del mismo palo, ambas cartas son del mismo valor!")

# Quien va ganando en la primera tirada...
if puntos_jugador_primera_tirada > puntos_croupier_primera_tirada:
    print("¡Enhorabuena, vas ganando jugador!")
else:
    if puntos_jugador_primera_tirada < puntos_croupier_primera_tirada:
        print("¡Noooo! ¡Vas perdiendo por ahora...! ¡Está ganando el croupier! ¡No te desesperes!")
    else:
        if puntos_jugador_primera_tirada == puntos_croupier_primera_tirada:
            print("¡Vaya vaya! ¡Estamos empatados en la primera tirada! ¡Esto está que arde!")

# Fin Comparativa
# Fin Primera Tirada

# Segunda Tirada
# Primera Tirada
print()
print('*'*60)
print(" ¡Segunda tirada de la mano! ¡Las cosas se ponen intensas!")
print('*'*60)
print()

# Reasignación de la variable A, que contiene el valor de los Ases
A = 1

# Selección de Cartas al Azar Segunda Tirada
valor_aleatorio_jugador_segundo_turno = random.choice(random.choice(tupla_de_todo))
print('La primera carta del jugador es: ', valor_aleatorio_jugador_segundo_turno, 'de',
      palo_aleatorio_jugador_segunda_tirada)
valor_aleatorio_croupier_segundo_turno = random.choice(random.choice(tupla_de_todo))
print('La primera carta del croupier es: ', valor_aleatorio_croupier_segundo_turno, 'de',
      palo_aleatorio_croupier_segunda_tirada)
# Fin Selección de Cartas al Azar

'''
# Primera tirada de cartas...
if puntaje_jugador_inicial == 0:
    puntaje_jugador_inicial += valor_aleatorio_del_1_al_10_jugador
puntaje_jugador_primer_turno = puntaje_jugador_inicial

if puntaje_crupier_inicial == 0:
    puntaje_crupier_inicial += valor_aleatorio_del_1_al_10_crupier
puntaje_crupier_primer_turno = puntaje_crupier_inicial

# Si ambos comparten el mismo palo en la primera tirada...
if palo_aleatorio_jugador == palo_aleatorio_crupier:
    print("¡La primera carta del jugador y del crupier es del mismo palo!")

# Si ambos son tanto del mismo palo como el mismo número en la primera tirada...
if palo_aleatorio_jugador == palo_aleatorio_crupier and puntaje_jugador_primer_turno == \
        puntaje_crupier_primer_turno:
    print("¡La primera carta del jugador y del crupier es tanto del mismo palo como del mismo valor!")


# Resultados
print("PRIMERA TIRADA JUGADOR: ", puntaje_jugador_primer_turno, "de ", palo_aleatorio_jugador,
      "; PRIMERA TIRADA CRUPIER: ", puntaje_crupier_primer_turno, "de ", palo_aleatorio_crupier)
'''
