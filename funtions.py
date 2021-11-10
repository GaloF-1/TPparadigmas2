import os


def borrar_consola():
    """
    Funcion que limpia la pantalla ( Solo disponible en windows o linux )
    :return: None
    """
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def set_jugador(vida, points, modo, name, bot):
    """
    Funcion que toma los parametros dados y los carga en un diccionario (jugador)
    :param vida: Vida del jugador INT
    :param points: puntos del jugador INT
    :param modo: Modo de jugego STR
    :param name: Nombre del jugador STR
    :param bot: si es un bot o no BOOL
    :return: Diccionario(jugador)
    """
    return {"vidas": vida, "puntaje": points, "mode": modo, "name": name, "bot": bot}


def validacion(tupla, texto, texto_alt):
    """
    Funcion que valida la entrada del usuario
    :param tupla: Tupla de valores que admite la entrada
    :param texto: Texto que orienta al usuario en las acciones que debe tomar STR
    :param texto_alt: Texto alternativo mostrado al no ingresar el valor dentro del rango pedido STR
    :return: Var, variable con el valor pedido dentro de la tupla
    """
    var = input(f"{texto}").lower()
    while var not in tupla:
        var = input(f"Por favor {texto_alt} ").lower()
    return var
