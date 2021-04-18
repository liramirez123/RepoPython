#Primera clase

class Gelatina:

    def __init__(self, tam, color, sabor) -> None:
        self.tam = tam
        self.color = color
        self.sabor = sabor

    def desplegar1(self) -> None:
        print(self.tam, self.color, self.sabor)


gel1 = Gelatina("chica","Rojo","sabor")
gel2 = Gelatina("mediana","amarilla","manzana")
gel3 = Gelatina("grande","azul", "mora")

gel1.desplegar1()
gel2.desplegar1()
gel3.desplegar1()


