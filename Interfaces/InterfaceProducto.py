
from Modelos.Lista import *
from Modelos.Producto import *
from Interfaces.Interface import *
from archivosJSON import archivosJSON
json = archivosJSON()


class InterfaceProducto(Interface):
    listaProductos = Lista()
    def __init__(self) -> None:
        super().__init__()
    def añadir(self):
        self.listaProductos.agregarElemento(
            Producto(
                input('Escribe el nombre del nuevo producto:\n'),
                input('Escribe el precio del nuevo producto:\n'),
                float(input('Escribe las unidades del nuevo producto:\n'))))   
        json.escribirProductos(self.listaProductos)
    
    def leer(self):
        if self.listaProductos.leerElementos() == True:
            return print('Lista Vacia')
        for prod in self.listaProductos.leerElementos():
            print(str(prod.Id) + "||" + prod.nombre + "||" + str(prod.precio)+ "||" + str(prod.cantidad))

    def eliminar(self):
        if self.listaProductos.leerElementos() == True:
            return print('Lista Vacia')
        p = self.listaProductos.eliminarElemento(input('Ingresa El nombre del producto a eliminar: '))
        if p == False:
            print('Elemento no encontrado')
        else:
            print('Producto eliminado')
        json.escribirProductos(self.listaProductos)
    
    def actualizar(self):
        p = self.listaProductos.buscarElemento(
            input('Ingresa el nombre del elemento a actualizar: \n'))
        if p == True:
            print('Lista Vacia')
        elif p == False:
            print('Elemento no encontrado')
        else:
            p.precio = float(input('Ingresa el nuevo precio del producto:\n'))
            p.cantidad = float(input('Ingresa el nuevo cantidad del producto:\n'))
            print('Producto:')
            print(str(p.Id) + "||" + p.nombre + "||" + str(p.precio)+ "||" + str(p.cantidad))
        json.escribirProductos(self.listaProductos)