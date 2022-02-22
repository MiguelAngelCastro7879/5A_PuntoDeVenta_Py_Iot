from Modelos.Venta import *
class Cliente:
    nombre=""
    Id = 0
    compra = None
    def __init__(self, nombre):
        self.nombre = nombre
        self.Id = id(self)
        self.compra = None
    
    def realizarCompra(self, productos):
        self.compra = Venta(productos,self)

    def añadirProducto(self, nombreProducto, cantidadProducto):
        return self.compra.añadirCesta(nombreProducto, cantidadProducto)
    
    def mostrarProductos(self):
        return self.compra.leerCesta()

    def quitarProducto(self, nombreProducto, cantidadProducto):
        return self.compra.eliminarCesta(nombreProducto, cantidadProducto)

    def finalizarCompra(self, efectivo, ListaVentas):
        self.compra.finalizar(efectivo)
        ListaVentas.agregarElemento(self.compra)
        return self.compra.leerCesta()