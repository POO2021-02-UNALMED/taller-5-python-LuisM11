#from zooAnimales.animalp import Animal
class Zona:
    
    def __init__(self, n=None,z=None,):
        self._nombre=n
        self._zoo=z
        self._animales=[]
        
    def agregarAnimales(self,a):
        self._animales.append(a)

    def cantidadAnimales(self):
        return len(self._animales)
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo