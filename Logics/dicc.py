def selecciondicc(modo):
    palabras = []
    if modo == "easy":
        with open("../resources/facil.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "medio":
        with open("../resources/medio.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "dificil":
        with open("../resources/dificil.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    return palabras