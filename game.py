import random, time
from funtions import borrar_consola


def gamerun(palabras, jugador):
    """
    Funcion que administra los modos de juego basados en la vida del jugador, facil, medio, dificil
    :param palabras: lista de palabras dependiente del modo del jugador
    :param jugador: diccionario con parametros  nombre, puntos, vida, bot, modo
    :return: None
    """
    word = random.choice(palabras)
    start = time.perf_counter()  # inicio del timer
    res = input(f"El jugador debe escribir {word} \nEscribe: ") if not jugador["bot"] else botCpu(jugador["mode"], word)

    if jugador["mode"] in ("medium", "easy"):
        word = word.upper()
        res = res.upper()

    perf = base_logic(word, res, start)
    punto = perf[0]
    tiempo = perf[1]

    if punto:
        jugador["puntaje"] += len(word)
        print("\nJugador {} ha acertado, suma {} puntos\n".format(jugador["name"], jugador["puntaje"]),
              "Tiempo {}\n".format(tiempo))
    else:
        jugador["vidas"] -= 1
        print("\nJugador {}, se equivoco y pierde una vida\n".format(jugador["name"]),
              "Vidas actuales {}\n".format(jugador["vidas"]))


def gamespeed(palabras, jugador):
    """
    Funcion que administra el modo de juego typespeed
    :param palabras: lista de palabras provenientes del archivo typespeed.txt
    :param jugador: Diccionario con parametros nombre, puntos, vida, bot, modo
    :return: None
    """
    contbuenas = 0
    timer = 0

    while timer < 60:
        p = random.choice(palabras)
        print(round(timer, 2))
        start = time.perf_counter()  # inicio del timer
        res = input(f"El jugador debe escribir {p} \nEscribe: ")if not jugador["bot"] else botCpu(jugador["mode"], p)

        perf = base_logic(p, res, start)
        punto = perf[0]
        tiempo = perf[1]

        if punto:
            contbuenas += 1
            print("nice")

        timer += tiempo
        borrar_consola()

    jugador["puntaje"] = round((contbuenas/60), 3)
    print("Jugador {}, tuvo un promedio de {} palabras por segundo".format(jugador["name"], jugador["puntaje"]))


def botCpu(mode, word):
    """
    Funcion que devuelve una la palabra acertada en funcion de un probabilidad dependiente del modo de juego del bot
    :param mode: Modo de juego del bot/ Modo de juego del usuario
    :param word: Palabra acertada
    :return: Palabra acertada o " " dependiendo de si se acierta o no
    """
    prob = random.random()

    time.sleep(0.5)

    if mode == "easy" and prob < 0.5:
        return word
    elif mode == "medium" and prob < 0.65:
        return word
    elif mode == "hard" or mode == "typespeed" and prob < 0.76:
        return word
    else:
        return " "


def base_logic(word, answer, start):
    """
    Funcion base de comparacion entre el imput del usuario y la palabra que a su vez calcula el tiempo de respuesta del
    usuario o maquina
    :param word: Palabra acertada
    :param answer: Palabra brindada por el usuario o bot
    :param start: Tiempo de inicio del timer
    :return: Tupla compuesta por un booleano y un float que representa el tiempo en el que el usuario ingresó la palabra
    """
    end = time.perf_counter()  # fin del timer
    cron = round(end - start, 2)

    if answer == word:
        if cron > 5:
            return False, cron
        else:
            return True, cron
    else:
        return False, cron
