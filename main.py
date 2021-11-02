import os
from Logics.gamesets import cargarjugadores
from Logics.gameplay import gameplay

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
    cargarjugadores()

