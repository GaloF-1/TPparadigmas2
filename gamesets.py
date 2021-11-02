import os
from gameplay import gameplay, gamespeed

def cargarjugadores():
    """
    Funcion que crea una lista de diccionarios(jugadores) seteando las caracteristicas de los mismos y posteriormente
    ejecuta el juego en el modo solicitado
    :return: NONE
    """

    # Establecer cantidad de jugadores humanos
    maxp = int(input("Ingrese la cantidad de usuarios: "))
    while maxp > 4 or maxp < 1:
        maxp = int(input("Por favor ingrese un numero entre 1 y 4: "))

    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    # Establecer cantidad de bots
    maxb = 0
    if maxp < 4:
        maxb = int(input(f"Ingrese la cantidad de bots de 0 a {4 - maxp}: "))
        while (4 - maxp) < maxb >= 0:
            maxb = int(input(f"Por favor ingrese un numero de 0 a {4 - maxp}: "))

    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    # Establecer modos de juego
    modos = ("easy", "medium", "hard", "typespeed")
    mod = input("Ingrese el modo de juego(easy, medium, hard): ")

    while mod.lower() not in modos:
        mod = input("Ingrese el modo de juego(easy, medium, hard): ")

    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    players = []  # lista de jugadores vacia

    # set de jugadores

    for i in range(maxp):
        if mod.lower() == "easy" or mod.lower() == "medium":
            players.append({"vidas": 5,
                            "puntaje": 0,
                            "mode": mod.lower(),
                            "name": input(f"ingrese nombre del jugador {i + 1}:"),
                            "bot": False})

        if mod.lower() == "hard" or mod.lower() == "typespeed":
            players.append({"vidas": 3,
                            "puntaje": 0,
                            "mode": mod.lower(),
                            "name": input(f"ingrese nombre del jugador {i + 1}:"),
                            "bot": False})

    # set de bots

    for i in range(maxb):
        if mod.lower() == "easy" or mod.lower() == "medium":
            players.append({"vidas": 5,
                            "puntaje": 0,
                            "mode": mod.lower(),
                            "name": f"bot{i + 1}",
                            "bot": True})

        if mod.lower() == "hard" or mod.lower() == "typespeed":
            players.append({"vidas": 3,
                            "puntaje": 0,
                            "mode": mod.lower(),
                            "name": f"bot{i + 1}",
                            "bot": True})

    if mod.lower() == "typespeed":
        gamespeed(players)
    else:
        gameplay(players)
