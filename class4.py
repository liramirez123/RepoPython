class Ejemplo:

    def publico(self):
        return "Soy un método público, a la vista de todos"

    def __privado(self):
        return "Soy un método privado, para ti no existo"

objeto = Ejemplo()

print(objeto.publico())
print(objeto._Ejemplo__privado())
