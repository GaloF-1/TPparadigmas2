from frontEnd import gameplay
from fileManagement import charge_players
from funtions import borrar_consola, set_jugador, validacion


def mainmenu():
    """
    Funcion de inicio de aplicacion, destinada a dirigir al usuario en opciones de nueva partida o cargar partida
    :return:
    """
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
        gameplay(charge_players())
    else:
        exit(-1)


def game_settings():
    """
    Set de parametros del juego, tales como la cantidad de usuarios y bots, modo de juego
    :return:
    """
    # Establecer cantidad de jugadores humanos
    maxp = int(input("Ingrese la cantidad de usuarios: "))
    while maxp > 4 or maxp < 0:
        maxp = int(input("Por favor ingrese un numero entre 0 y 4: "))

    # Establecer cantidad de bots
    maxb = 0
    if maxp < 4:
        maxb = int(input(f"Ingrese la cantidad de bots de 0 a {4 - maxp}: "))
        while (4 - maxp) < maxb >= 0:
            maxb = int(input(f"Por favor ingrese un numero de 0 a {4 - maxp}: "))

    borrar_consola()

    # Establecer modos de juego
    modos = ("easy", "medium", "hard", "typespeed")
    mod = validacion(modos, f"Ingrese el modo de juego{modos}: ",
                            f"Por favor ingrese uno de los modos {modos}")

    cargar_jugadores(maxp, maxb, mod)


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
                                   False if i < maxp else True))
        borrar_consola()

    gameplay(players)
