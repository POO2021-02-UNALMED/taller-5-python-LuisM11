from zooAnimales.animalp import Animal

class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0
    def __init__(self,n=None,e=0,h=None,g=None,ce=None,ca=None):
        super().__init__(n,e,h,g)
        self._colorEscamas=ce
        self._cantidadAletas=ca
        Pez.listado.append(self)
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    @classmethod
    def crearSalmon(cls,n,e,g):
        cls.salmones+=1
        return cls(n,e,"oceano",g,"rojo",6)
    @classmethod
    def crearBacalao(cls,n,e,g):
        cls.bacalaos+=1
        return cls(n,e,"oceano",g,"gris",6)
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def movimiento(self):
        return "nadar"