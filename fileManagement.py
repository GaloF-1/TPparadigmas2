from funtions import set_jugador


def selecciondicc(modo):

    palabras = []

    with open(f"{modo}.txt", "r") as archivo:
        for i in archivo:
            palabras.append(i.strip())

    return palabras


def charge_players():
    players = []
    with open("games.txt", "r") as archivo:
        for i in archivo:
            i = i.strip().split(" ")
            players.append(set_jugador(int(i[0]), int(i[1]), i[2], i[3], bool(i[4])))

    return players
