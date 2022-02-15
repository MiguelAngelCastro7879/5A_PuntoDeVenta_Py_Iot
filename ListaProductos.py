from Lista import * 
from archivosJSON import *

class ListaProductos(Lista):
    def __init__(self):
        super().__init__()
    def agregarProducto(self, Producto):
        self.agregarElemento(Producto)
        ajs = archivosJSON()
        ajs.añadirProducto(Producto)
    def eliminarProducto(self, productoNombre):
        p = self.buscarProducto(productoNombre)
        if p != False and p !=True:
            self.eliminarElemento(self.buscarProducto(productoNombre))
        else: return p

    def leerProductos(self):
        return self.leerElementos()

    def buscarProducto(self, productoNombre):
        if self.leerElementos() == True:
            return True
        for elemento in self.leerElementos():
            if elemento.nombre == productoNombre:
                return elemento
        return False