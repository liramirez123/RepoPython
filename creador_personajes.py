import uuid
import json
import time
from pj import personajes


class Personaje:

    def __init__(self, nombre, raza, clase, vida, mana):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self. mana = mana

    def configurarPersonaje(self):
        print("""\n ¿Qué personaje desea crear?\n
                1) Humanos
                2) Orcos""")
        raza = input("\n>")
        if raza == '1':
            raza = "Humanos"
            print("""\n¿Qué clase de humano desear crar?\n
                 1) Guerrero
                 2) Jinete
                 3) Mago""")
            clase = input("\n>")
            if clase == '1':
                clase = 'Guerrero'
                # Llamamos un metodo que ccree el personaje
            elif clase == '2':
                clase ='Jinete'
                # Llamamos un metodo que cree al personaje
            elif clase == '3':
                clase ='Mago'
                # Llamamos un metodo que cree al personaje
        elif raza == '2':
            raza ='Orcos'
            print("""\n ¿Qué clase de orcos desea cear?\n
                    1) Guerrero
                    2) Chaman
                    3) Jinete""")
            raza = input("\n>")
            if clase == '1':
                clase = 'Guerrero'
                # Llamamos un metodo que cree el personaje
            elif clase == '2':
                clase = 'Chaman'
                # Llamamos un metodo que que cree el personaje
            elif clase == '3':
                 clase = 'Jinete'
                # Llamamos un metodo que cree el personaje
        else:
            print("\nHas introducido un comando incorrecto")
