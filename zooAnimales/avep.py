from zooAnimales.animalp import Animal

class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0
    def __init__(self,n=None,e=0,h=None,g=None,c=None):
        super().__init__(n,e,h,g)
        self._colorPlumas=c
        Ave.listado.append(self)
    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)
    def __str__(self):
        return "volar"
    @classmethod
    def crearHalcon(cls,n,e,g):
        cls.halcones=+1
        return cls(n,e,"montanas",g,"cafe glorioso")
    @classmethod
    def crearAguila(cls,n,e,g):
        cls.aguilas=+1
        return Ave(n,e,"montanas",g,"blanco y amarillo")
    def getColorPlumas(self):
        return self._colorPlumas
    
