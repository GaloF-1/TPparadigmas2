from funtions import set_jugador


def selecciondicc(modo):
    """
    Funcion que llama a un archivo dependiendo del modo de juego seleccionado y coloca su contenido en una lista
    :param modo: string dentro de la tupla (easy, medium, hard)
    :return: lista de palabras(strings)
    """
    palabras = []

    with open(f"{modo}.txt", "r") as archivo:
        for i in archivo:
            palabras.append(i.strip())

    return palabras


def savegame(players):
    """
    Funcion que guarda en un archivo la partida en ejecucion, siendo partida la lista de jugadores(diccionarios)
    :param players: Lista de diccionarios
    :return: None
    """
    with open("games.txt", "w") as save:
        for i in players:
            values = i.values()
            for j in values:
                save.write(str(j) + " ")
            save.write("\n")


def charge_players():
    """
    Funcion que llama al archivo games y carga en una lista su contenido previamente convertido en un diccionario
    :return: diccionario de jugadores
    """
    players = []  # lista de jugadores
    with open("games.txt", "r") as archivo:
        for i in archivo:
            i = i.strip().split(" ")
            players.append(set_jugador(int(i[0]), int(i[1]), i[2], i[3], eval(i[4])))

    return players
