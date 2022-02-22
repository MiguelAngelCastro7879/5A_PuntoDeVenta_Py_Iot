from Interfaces.InterfaceCliente import *
from Interfaces.InterfaceProducto import *
from Interfaces.InterfaceVentas import *

clientes = InterfaceCliente()
productos = InterfaceProducto()
ventas = InterfaceVentas()


class Acciones:
    def __init__(self, menu1, menu2):
        if menu2 == '0':
            pass
        elif menu1 == '1' and menu2 == '1':
            productos.añadir()
        elif menu1 == '1' and menu2 == '2':
            productos.leer()
        elif menu1 == '1' and menu2 == '3':
            productos.eliminar()
        elif menu1 == '1' and menu2 == '4':
            productos.actualizar()
        elif menu1 == '2' and menu2 == '1':
            clientes.añadir()
        elif menu1 == '2' and menu2 == '2':
            clientes.leer()
        elif menu1 == '2' and menu2 == '3':
            clientes.eliminar()
        elif menu1 == '2' and menu2 == '4':
            clientes.actualizar()
        elif menu1 == '3' and menu2 == '1':
            ventas.añadir()
        elif menu1 == '3' and menu2 == '2':
            ventas.leer()
        elif menu1 == '3' and menu2 == '3':
            ventas.devVenta()
        input()