from zooAnimales.animal import Animal

class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0
    def __init__(self,n=None,e=0,h=None,g=None,ce=None,lc=None):
        super().__init__(n,e,h,g)
        self._colorEscamas=ce
        self._largoCola=lc
        Reptil.listado.append(self)
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    @classmethod
    def crearIguana(cls,n,e,g):
        cls.iguanas=+1
        return cls(n,e,"humedal",g,"verde",3)
    @classmethod
    def crearSerpiente(cls,n,e,g):
        cls.serpientes=+1
        return cls(n,e,"jungla",g,"blanco",1)
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    def __str__(self):
        return "reptar"