from zooAnimales.animalp import Animal

class Mamifero(Animal):
    listado=[]
    caballos=0
    leones=0
    def __init__(self,n=None,e=0,h=None,g=None,pe=None,pa=None):
        super().__init__(n,e,h,g)
        self._pelaje=pe
        self._patas=pa
        Mamifero.listado.append(self)
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.listado)
    @classmethod
    def crearCaballo(cls,n,e,g):
        cls.caballos+=1
        return Mamifero(n,e,"pradera",g,True,4)
    @classmethod
    def crearLeon(cls,n,e,g):
        cls.leones+=1
        return Mamifero(n,e,"selva",g,True,4)
    def getPatas(self):
        return self._patas
    def isPelaje(self):
        return self._pelaje
