import random, time, os
from dicc import selecciondicc


def gameplay(players):
    """Funcion que ejecuta el juego propiamente dicho en el modo "supervivencia"
    :param players: lista de diccionarios con datos criticos de cada jugador(vidas, modo de juego, puntaje)
    :return: NONE
    """

    for i in players:

        # validacion para empezar a jugar
        run = input("Jugador {} ingrese ok para comenzar: ".format(i["name"]))
        while run.lower() != "ok":
            run = input("Jugador {} ingrese ok para comenzar: ".format(i["name"]))

        # Seleccion de diccionarios
        palabras = selecciondicc(i["mode"])

        while i["vidas"] > 0:
            word = palabras[random.randint(0, len(palabras) - 1)]
            start = time.perf_counter()  # inicio del timer
            answer = input(f"El jugador debe escribir {word} \nEscribe: ")

            if i["mode"] in ("medium", "easy"):
                word = word.upper()
                answer = answer.upper()

            if answer == word:
                end = time.perf_counter()  # fin del timer
                print(f"Tiempo: {round(end - start, 2)} ")
                if end - start > 5:
                    i["vidas"] -= 1
                    print("Vidas: {}".format(i["vidas"]))
                else:
                    i["puntaje"] += len(word)
            else:
                i["vidas"] -= 1
                print("Vidas: {}".format(i["vidas"]))

            os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        print("jugador {indice} puntos {puntos}".format(indice=i["name"], puntos=i["puntaje"]))


def gamespeed(players):
    """
    Funcion que ejecuta el modo de juego typespeed
    :param players: lista de diccionarios con datos criticos de cada jugador(vidas, modo de juego, puntaje)
    :return: NONE
    """

    for i in players:

        # validacion para empezar a jugar
        run = input("Jugador {} ingrese ok para comenzar: ".format(i["name"]))
        while run.lower() != "ok":
            run = input("Jugador {} ingrese ok para comenzar: ".format(i["name"]))

        # Seleccion de diccionarios
        palabras = selecciondicc(i["mode"])
        contbuenas = 0
        timer = 0

        while timer < 60:
            a = palabras[random.randint(0, len(palabras) - 1)]
            print(round(timer, 2))
            start = time.perf_counter()  # inicio del timer
            answer = input(f"El jugador debe escribir {a} \nEscribe: ")
            end = time.perf_counter()  # fin del timer

            if answer == a:
                contbuenas += 1

            timer += (end - start)
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        print("Jugador {}, tuvo un promedio de {} palabras por segundo".format(i["name"], round((contbuenas/60), 2)))


gameplay([{"vidas": 3, "puntaje": 0, "mode": "medium", "name": "Galo", "bot": False}])
