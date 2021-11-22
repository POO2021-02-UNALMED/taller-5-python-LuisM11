from zooAnimales.animalp import Animal

class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    def __init__(self,n=None,e=0,h=None,g=None,c=None,v=None):
        super().__init__(n,e,h,g)
        self._colorPiel=c
        self._venenoso=v
        Anfibio.listado.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    def __str__(self):
        return "saltar"
    @classmethod
    def crearRana(cls,n,e,g):
        cls.ranas=+1
        return Anfibio(n,e,"selva",g,"rojo",True)
    @classmethod
    def crearSalamandra(cls,n,e,g):
        cls.salamandras=+1
        return Anfibio(n,e,"selva",g,"negro y amarillo",False)
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
