from asyncio.windows_events import NULL
from Lista import * 

class ListaVentas(Lista):
    def __init__(self):
        super().__init__()
    def agregarVenta(self, Venta):
        self.agregarElemento(Venta)
        
    def leerVentas(self):
        return self.leerElementos()

    def buscarVenta(self, ventaId):
        if self.leerElementos() == True:
            return True
        for elemento in self.leerElementos():
            if elemento.Id == ventaId:
                return elemento
        return False