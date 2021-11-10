import random, time
from funtions import borrar_consola


def gamerun(palabras, jugador):
    word = palabras[random.randint(0, len(palabras) - 1)]
    start = time.perf_counter()  # inicio del timer
    answer = input(f"El jugador debe escribir {word} \nEscribe: ")

    if jugador["mode"] in ("medium", "easy"):
        word = word.upper()
        answer = answer.upper()

    if answer == word:
        end = time.perf_counter()  # fin del timer
        print(f"Tiempo: {round(end - start, 2)} ")
        if end - start > 5:
            jugador["vidas"] -= 1
            print("Vidas: {}".format(jugador["vidas"]))
        else:
            jugador["puntaje"] += len(word)
    else:
        jugador["vidas"] -= 1
        print("Vidas: {}".format(jugador["vidas"]))


def gamespeed(palabras, jugador):

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
        borrar_consola()

    jugador["puntaje"] = round((contbuenas/60))
    print("Jugador {}, tuvo un promedio de {} palabras por segundo".format(jugador["name"], jugador["puntaje"], 2))
