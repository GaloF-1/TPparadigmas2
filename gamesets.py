import os
from frontEnd import gameplay
from fileManagement import charge_players
from funtions import borrar_consola, set_jugador


def mainmenu():
    choice = int(input("Bienvenido a Pytespeed\n"
                       "\n"
                       "1) Nueva partida\n"
                       "2) Cargar Partida\n"
                       "3) Salir\n"
                       "\n"))

    borrar_consola()

    while choice not in (1, 2, 3):
        choice = int(input("Seleccione una opcion por favor\n"
                           "\n"
                           "1) Nueva partida\n"
                           "2) Cargar Partida\n"
                           "3) Salir\n"
                           "\n"))

        borrar_consola()

    if choice == 1:
        game_settings()
    elif choice == 2:
        game_charge()
    else:
        exit(-1)


def game_settings():
    # Establecer cantidad de jugadores humanos
    maxp = int(input("Ingrese la cantidad de usuarios: "))
    while maxp > 4 or maxp < 1:
        maxp = int(input("Por favor ingrese un numero entre 1 y 4: "))

    # Establecer cantidad de bots
    maxb = 0
    if maxp < 4:
        maxb = int(input(f"Ingrese la cantidad de bots de 0 a {4 - maxp}: "))
        while (4 - maxp) < maxb >= 0:
            maxb = int(input(f"Por favor ingrese un numero de 0 a {4 - maxp}: "))

    borrar_consola()

    # Establecer modos de juego
    modos = ("easy", "medium", "hard", "typespeed")
    mod = input("Ingrese el modo de juego(easy, medium, hard, Typespeed): ").lower()

    while mod not in modos:
        mod = input("Ingrese el modo de juego(easy, medium, hard): ").lower()

    cargar_jugadores(maxp, maxb, mod)


def game_charge():
    gameplay(charge_players())


def cargar_jugadores(maxp, maxb, mod):
    """
    Funcion que crea una lista de diccionarios(jugadores) seteando las caracteristicas de los mismos y posteriormente
    ejecuta el juego en el modo solicitado
    :return: NONE
    """
    players = []  # lista de jugadores vacia

    # set de jugadores y bots

    for i in range(maxp + maxb):
        players.append(set_jugador(5 if mod in ("easy", "medium") else 3, 0, mod,
                                   input(f"ingrese nombre del jugador {i + 1}:") if i < maxp else f"bot {i + 1}",
                                   True if i > maxp else False))
        borrar_consola()

    gameplay(players)
