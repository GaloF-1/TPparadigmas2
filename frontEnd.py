from fileManagement import selecciondicc
from game import gamerun, gamespeed
from funtions import set_jugador, savegame


def gameplay(players):

    # Juego
    for i in players:

        # validacion para empezar a jugar
        des = input("Jugador {} ingrese ok para comenzar: ".format(i["name"]))
        while des.lower() not in ("ok", "salir"):
            des = input("Jugador {} ingrese ok o salir: ".format(i["name"]))

        if des == "salir":
            savegame(players)

        # Seleccion de diccionarios
        palabras = selecciondicc(i["mode"])

        while i["vidas"] > 0:
            if i["mode"] != "typespeed":
                gamerun(palabras, i)
            else:
                gamespeed(palabras, i)

        print("jugador {} game over".format(i["name"]))

    scoreboard(players)


def scoreboard(players):

    winer = set_jugador(0, 0, "", "", False)

    for i in players:
        print("Jugador {}, puntos: {}".format(i["name"], i["puntaje"]))
        if i["puntaje"] > winer["puntaje"]:
            winer = i

    print("Ganador, {}".format(winer["name"]))
