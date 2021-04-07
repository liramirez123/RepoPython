class Fraccion:

    def __init__(self,arriba,abajo):
        self.num = arriba
        self.den = abajo

    def mostrar(self):
        print(self.num,"/",self.den)
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otraFraccion):
        nuevoNum = self.num * otraFraccion.den + self.den * otraFraccion.num
        nuevoDen = self.den * otraFraccion.den

        return Fraccion(nuevoNum,nuevoDen)


miF = Fraccion(1,2)
miF.mostrar()

f1 = Fraccion(1,4)
f2 = Fraccion(1,2)
f3 = f1 + f2
print(f3)