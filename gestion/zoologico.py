class Zoologico:
    _zonas=[]
    def __init__(self,n=None,u=None):
        self._nombre=n
        self._ubicacion=u
    def agregarZonas(self,z):
        Zoologico._zonas.append(z)
    def cantidadTotalAnimales(self):
        c=0
        for i in  Zoologico._zonas:
            c+= i.cantidadAnimales()
        return c
    def getZona(self):
        return Zoologico._zonas
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion