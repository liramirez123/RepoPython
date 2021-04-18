#Segunda clase

class Television:

    def __init__(self,marca) -> None:
        self.marca = marca
        self.encendida = True

    def EncenderTv(self):
        if self.encendida == False:
            self.encendida = True
        else:
            print("La televisión ya está encendida")
    
    def apagarTv(self):
        if self.encendida == True:
            self.encendida = False
        else:
            print("La televisión ya esta encendida")
    
    def saberMarca(self):
        print(self.marca)


tele = Television("Sansung")
tele.EncenderTv()
tele.apagarTv()
tele.saberMarca()
