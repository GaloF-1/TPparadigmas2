def selecciondicc(modo):

    palabras = []

    if modo == "easy":
        with open("easy.txt", "r") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "medium":
        with open("medium.txt", "r") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))
    elif modo == "hard" or modo == "typespeed":
        with open("hard.txt", "r") as archivo:
            for i in archivo:
                palabras.append(i.replace("\n", ""))

    return palabras

# print(selecciondicc("easy"))