#Herencia 

class Electrodomestico:

    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.estado = False
    
    def encenderElec(self):
        if self.estado == False:
            self.estado = True
            print("Se ha encendido "+ self.nombre)
        else:
            print("El electrodomestico ya esta encendido")
    
    def apagarElec(self):
        if self.estado == True:
            self.estado = False
            print("Se ha apagado "+ self.nombre)
        else:
            print("El electrodomestico ya esta apagado")

class Celular(Electrodomestico):

    def mandarMensaje(self):
        if self.estado == True:
            print("Llamando")


class Television(Electrodomestico):

    def cambiarCanal(self):
        print("Cambiando de canal")


cel = Celular("Iphone")
cel.encenderElec()
cel.mandarMensaje()
cel.apagarElec()
tel = Television("Television LG")
tel.encenderElec()
tel.cambiarCanal()
tel.apagarElec()


