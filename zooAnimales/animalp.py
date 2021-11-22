
class Animal:
    totalAnimales=0
    def __init__(self,n=None,e=0,h=None,g=None,z=None):
        self.nombre=n
        self.edad=e
        self.habitat=h
        self.genero=g
        self.zona=z
        Animal.totalAnimales+=1
    def movimiento (self):
        return "desplazarse"
    @classmethod
    def totalPorTipo(cls):
        from gestion.zonap import Zona
        from zooAnimales.anfibiop import Anfibio
        from zooAnimales.mamiferop import Mamifero
        from zooAnimales.avep import Ave
        from zooAnimales.reptilp import Reptil
        from zooAnimales.pezp import Pez
        return "Mamiferos : "+str(Mamifero.cantidadMamiferos())+ "\n" + "Aves : " +str(Ave.cantidadAves())+ "\n" + "Reptiles : " + str(Reptil.cantidadReptiles())+ "\n" + "Peces : " + str(Pez.cantidadPeces()) +"\n" + "Anfibios : "+str(Anfibio.cantidadAnfibios())
    
    def toString(self):
        return "Mi nombre es "+str(self.getNombre()) + ", tengo una edad de "+ str(self.getEdad())+ ", habito en "+ str(self.getHabitat())+ " y mi genero es "+str(self.getGenero())
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getHabitat(self):
        return self.habitat
    def getZona(self):
        return self.zona
    def getGenero(self):
        return self.genero