import os


def borrar_consola():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def set_jugador(vida, points, modo, name, bot):
    return {"vidas": vida, "puntaje": points, "mode": modo, "name": name, "bot": bot}


def savegame(players):
    with open("games.txt", "w") as save:
        for i in players:
            values = i.values()
            for j in values:
                save.write(str(j) + " ")
            save.write("\n")

    exit(-1)
