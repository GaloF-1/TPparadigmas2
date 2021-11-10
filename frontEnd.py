from fileManagement import selecciondicc, savegame
from game import gamerun, gamespeed
from funtions import set_jugador, validacion


def gameplay(players):
    """
    Funcion que recorre una lista de jugadores(Diccionarios), valida al usuario y ejecuta el modo de juego
    correspondiente al jugador actual
    :param players: Lista de jugadores(Diccionarios)
    :return: None
    """
    # Juego
    for i in players:

        # Seleccion de diccionarios
        palabras = selecciondicc(i["mode"])

        if not i["bot"]:
            # validacion para empezar a jugar
            validacion("ok", "Jugador {} ingrese ok para comenzar: ".format(i["name"]),
                             "Jugador {} ingrese ok para comenzar: ".format(i["name"]))

        if i["mode"] != "typespeed":
            while i["vidas"] > 0:
                gamerun(palabras, i)
                savegame(players)
        else:
            gamespeed(palabras, i)
            savegame(players)

        print("\njugador {} game over".format(i["name"]))

    scoreboard(players)


def scoreboard(players):
    """
    Funcion que imprime los resultados del juego una vez que se haya recorrido toda la lista, y muestra el jugador o
    jugadores que hayan ganado (En caso de haber un empate)
    :param players: Lista de jugadores(diccionarios)
    :return: None
    """
    winer = set_jugador(0, 0, "", "", False)

    for i in players:
        print("Jugador {}, puntos: {}".format(i["name"], i["puntaje"]))
        if i["puntaje"] > winer["puntaje"]:
            winer = i
        elif i["puntaje"] == winer["puntaje"]:
            winer["name"] += " " + i["name"]

    print("Ganador/es, {}".format(winer["name"]))
