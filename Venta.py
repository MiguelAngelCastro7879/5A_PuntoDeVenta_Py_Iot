from re import I
from ListaClientes import *
from ListaProductos import *
from Producto import *
class Venta:
    ProductosGenerales = None
    ListaProductos = ListaProductos()
    Cliente = None
    estado = 'No realizada'
    total = 0
    efectivo = 0
    cambio = 0
    Id = 0

    def __init__(self, productos, Cliente):
        self.ListaProductos = ListaProductos()
        self.Id = id(self)
        self.ProductosGenerales = productos
        self.Cliente = Cliente
        self.estado = 'No realizada'
        self.total = 0
        self.efectivo = 0
        self.cambio=0
    
    def añadirCesta(self, nombreProducto, cantidadProducto):
        if cantidadProducto <= 0:
            return True
        x = self.ProductosGenerales.buscarProducto(nombreProducto)
        if x != True and x !=False:
            if  x.cantidad >= cantidadProducto:
                x.cantidad = x.cantidad - cantidadProducto
            else:
                cantidadProductoNegada = cantidadProducto-x.cantidad
                cantidadProducto = cantidadProducto - cantidadProductoNegada
                x.cantidad = 0
            
            pnuevo = Producto(x.nombre, x.precio, cantidadProducto)
            
            self.ListaProductos.agregarProducto(pnuevo)
            return pnuevo
        return x

    def eliminarCesta(self, nombreProducto, cantidadProducto):
        pg = self.ProductosGenerales.buscarProducto(nombreProducto)
        x = self.ListaProductos.buscarProducto(nombreProducto)
        if x != True and x !=False:
            if  x.cantidad >= cantidadProducto:
                x.cantidad = x.cantidad - cantidadProducto
                pg.cantidad = pg.cantidad + cantidadProducto
            elif cantidadProducto >=  x.cantidad:
                self.ListaProductos.eliminarElemento(x)
        
    def leerCesta(self):
        return self.ListaProductos.leerProductos()
    def devolucion(self):
        for x in self.ListaProductos.leerProductos():
            for pg in  self.ProductosGenerales.leerProductos():
                if pg.nombre == x.nombre:
                    pg.cantidad = pg.cantidad + x.cantidad
                    self.estado = 'Devolucion'

    def calcularTotal(self):
        for x in self.ListaProductos.leerProductos():
            self.total = float(self.total) + (float(x.precio) * float(x.cantidad))
            
        return self.total
    def finalizar(self, efectivo):
        self.calcularTotal()
        self.efectivo = efectivo
        self.cambio = self.efectivo - self.total
        self.estado = 'Finalizada'
        return self.cambio

