import random


def generacion_carta():
    numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
    nombre = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "AS")
    palo = ("Corazon", "Trebol", "Picas", "Diamante")
    x = random.randint(0, 12)
    y = random.randint(0, 3)
    carta_obtenida = (numero[x], nombre[x], palo[y])
    carta_mismo_numero = (numero[x], palo[y])

    if str(numero[x]) == nombre[x]:
        return carta_mismo_numero
    else:
        return carta_obtenida


def validacion(monto):
    if 100000 >= monto + pozo > 0 and monto != 0:
        return monto
    return 0


def jugar_una_mano():
    pass


pozo = 0
nombre = input("Ingrese su nombre: ")
opcion = None

while pozo <= 0 or pozo > 100000:
    valor = int(input("Ingrese el monto inicial del pozo: "))
    pozo += validacion(valor)

while opcion != "0":
    print("1) Apostar\n2)Jugar una mano\n0)Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        valor = int(input("Ingrese el monto para sumar al pozo: "))
        pozo += validacion(valor)
    elif opcion == "2":
        apuesta_mano = int(input("Ingrese la apuesta para esta mano: "))
        if pozo >= apuesta_mano > 0 == apuesta_mano % 5:
            jugar_una_mano()
    elif opcion == "0":
        print(f'{nombre} esperamos que haya disfrutado su juego')
