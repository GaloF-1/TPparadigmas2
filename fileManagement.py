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


def charge_players():
    """
    Funcion que llama al archivo games y carga en una lista su contenido previamente convertido en un diccionario
    :return:
    """
    players = []
    with open("games.txt", "r") as archivo:
        for i in archivo:
            i = i.strip().split(" ")
            players.append(set_jugador(int(i[0]), int(i[1]), i[2], i[3], bool(i[4])))

    return players
