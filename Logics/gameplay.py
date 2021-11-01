import random
import time
import os
import dicc

def gameplay(players):
    """Funcion que ejecuta el juego propiamente dicho
    :param players: lista de diccionarios datos criticos de cada jugador(vidas, modo de juego, puntaje)
    :return: NONE
    """

    # funcion que limpia la consola de python
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    for i in players:
        # Seleccion de diccionarios
        palabras = dicc.selecciondicc(i["mode"])

        while i["vidas"] > 0:
            a = palabras[random.randint(0, len(palabras) - 1)]
            start = time.perf_counter()  # inicio del timer
            answer = input(f"El jugador debe escribir {a} \nEscribe: ")

            if i["mode"] == "easy" or i["mode"] == "medio":
                a = a.upper()
                answer = answer.upper()

            if answer == a:
                end = time.perf_counter()  # fin del timer
                print(f"Tiempo: {round(end - start, 2)} ")
                if end - start > 5:
                    i["vidas"] -= 1
                    print("Vidas: {}".format(i["vidas"]))
                else:
                    i["puntaje"] += len(a)
            else:
                i["vidas"] -= 1
                print("Vidas: {}".format(i["vidas"]))

            clearConsole()

        print("jugador {indice} puntos {puntos}".format(indice=i["nombre"], puntos=i["puntaje"]))


gameplay([{"vidas": 3, "puntaje": 0, "mode": "medio", "nombre": "Galo", "bot": False}])
