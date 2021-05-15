class Ejemplo:

    def __init__(self):
        self.__oculto ="Me encuentro oculto en la clase"

    def publico(self):
        return "Soy un método públio, a la vista de todos"
    def __privado(self):
        return "Soy un método privado, para tí no existo"
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = Ejemplo()

print(objeto.publico())

print(objeto._Ejemplo__privado())

print(objeto.get_oculto())

objeto.set_oculto()