from zooAnimales.animalp import Animal
class Zona:
    _animales=[]
    def __init__(self, n=None,z=None,):
        self._nombre=n
        self._zoo=z
        
    def agregarAnimales(self,a):
        Zona._animales.append(a)

    def cantidadAnimales(self):
        return len(Zona._animales)
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo