import os
from Logics import gamesets
from Logics import gameplay

choice = int(input("Bienvenido a Pytespeed\n"
                   "\n"
                   "1) Nueva partida\n"
                   "2) Cargar Partida\n"
                   "3) Salir\n"
                   "\n"))

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

while choice not in (1, 2, 3):
    choice = int(input("Seleccione una opcion por favor\n"
                       "\n"
                       "1) Nueva partida\n"
                       "2) Cargar Partida\n"
                       "3) Salir\n"
                       "\n"))

    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if choice == 1:
    gameplay.gameplay([{"vidas": 3, "puntaje": 0, "mode": "medium", "nombre": "Galo", "bot": False}])

if choice == 2:
    gameplay.gameplay()
