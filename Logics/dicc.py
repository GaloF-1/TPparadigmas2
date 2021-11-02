

def selecciondicc(modo):

    palabras = []

    if modo == "easy":
        with open("../../recursos/1easy.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "medium":
        with open("../../recursos/medium.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "hard":
        with open("../../recursos/hard.txt", "rt") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))

    return palabras
