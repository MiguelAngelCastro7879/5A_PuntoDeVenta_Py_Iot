import os
from ListaClientes import *
from ListaProductos import *
from Producto import *
from Cliente import *
from Venta import *
from ListaVentas import *
productos = ListaProductos()
cliente = ListaClientes()
ventas = ListaVentas()

class Acciones:
    def __init__(self, menu1, menu2):
        if menu2 == '0':
            pass
        elif menu1 == '1' and menu2 == '1':
            self.aProducto()
        elif menu1 == '1' and menu2 == '2':
            self.lProductos()
        elif menu1 == '1' and menu2 == '3':
            self.eProducto()
        elif menu1 == '1' and menu2 == '4':
            self.actProducto()
        elif menu1 == '2' and menu2 == '1':
            self.aCliente()
        elif menu1 == '2' and menu2 == '2':
            self.lClientes()
        elif menu1 == '2' and menu2 == '3':
            self.eCliente()
        elif menu1 == '2' and menu2 == '4':
            self.actCliente()
        elif menu1 == '3' and menu2 == '1':
            self.aVenta()
        elif menu1 == '3' and menu2 == '2':
            self.lVentas()
        elif menu1 == '3' and menu2 == '3':
            self.devVenta()
        input()

    def aProducto(self):
        productos.agregarProducto(
            Producto(
                input('Escribe el nombre del nuevo producto:\n'),
                input('Escribe el precio del nuevo producto:\n'),
                float(input('Escribe las unidades del nuevo producto:\n'))))   
    
    def lProductos(self):
        if productos.leerProductos() == True:
            return print('Lista Vacia')
        for prod in productos.leerProductos():
            print(str(prod.Id) + "||" + prod.nombre + "||" + str(prod.precio)+ "||" + str(prod.cantidad))
    
    def eProducto(self):
        if productos.leerProductos() == True:
            return print('Lista Vacia')
        p = productos.eliminarProducto(input('Ingresa El nombre del producto a eliminar: '))
        if p == False:
            print('Elemento no encontrado')
        else:
            print('Producto eliminado')
    
    def actProducto(self):
        p = productos.buscarProducto(
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
 
    def aCliente(self):
        cliente.agregarCliente(
            Cliente(
                input('Escribe el nombre del nuevo Cliente:\n')))   
    
    def lClientes(self):
        if cliente.leerClientes() == True:
            return print('Lista Vacia')
        for client in cliente.leerClientes():
            print(str(client.Id) + "||" + client.nombre )
    
    def eCliente(self):
        if cliente.leerClientes()== True:
            return print('Lista Vacia')
        c = cliente.eliminarCliente(input('Ingresa El nombre del Cliente a eliminar: '))
        if c == False:
            print('Elemento no encontrado')
        else:
            print('Cliente eliminado')
    
    def actCliente(self):
        c = cliente.buscarCliente(
            input('Ingresa el nombre del cliente a actualizar: \n'))
        if c == True:
            print('Lista Vacia')
        elif c == False:
            print('Cliente no encontrado')
        else:
            c.nombre = input('Ingresa el nuevo nombre del Cliente:\n')
            print('Cliente:')
            print(str(c.Id) + "||" + c.nombre)
    
    def aVenta(self):
        client = cliente.buscarCliente(
            input('Ingresa el nombre del cliente:\n'))
        if client== True or client == False:
            return print('Cliente no encontrado')
        else:
            client.realizarCompra(productos)
            opc = 1
            while opc !=0:
                os.system('cls')
                print("  VENTA "+str(client.compra.Id)+"\
                            \n//////////////////\
                            \n[1]Añadir Producto\
                            \n[2]Eliminar Producto\
                            \n[3]Listado de Productos\
                            \n[4]Finalizar Venta\
                            \n[0]CANCELAR VENTA")
                opc = input()
                if opc == '1': 
                    c = client.añadirProducto(
                        input('Ingresa el nombre del producto: '), 
                        float(input('Ingresa la cantidad de productos: ')))
                    if c == True: return print('No hay productos en el almacen')
                    if c == False: print('Elemento no encontrado')
                    else: print(str(c.Id) + "||" + c.nombre + "||" + str(c.precio)+ "||" + str(c.cantidad))
                
                elif opc == '2':
                    c = client.quitarProducto(
                        input('Ingresa el nombre del producto: '), 
                        float(input('Ingresa la cantidad de productos: ')))
                    if c == True: return print('Lista Vacia')
                    if c == False: print('Elemento no encontrado')
                    else: print('Elementos Eliminados')
                elif opc == '3':
                    cl = client.mostrarProductos()
                    if cl == True: return print('Lista Vacia')
                    for c in cl:
                        print(str(c.Id) + "||" + c.nombre + "||" + str(c.precio)+ "||" + str(c.cantidad))
                elif opc == '4':
                    cl = client.mostrarProductos()
                    if cl == True: return print('Lista Vacia')
                    print('Cliente: ' + str(client.nombre))
                    print('Folio: ' + str(client.compra.Id))
                    for c in cl:
                        print(str(c.Id) + "||" + c.nombre + "||" + str(c.precio)+ "||" + str(c.cantidad))
                    client.finalizarCompra(float(input('Ingresa el efectivo del cliente: ')), ventas)
                    print('Total: ' + str(client.compra.total))
                    print('Efectivo: ' + str(client.compra.efectivo))
                    print('Cambio: ' + str(client.compra.cambio))
                    opc = 0
                input()

    def lVentas(self):
        if ventas.leerVentas() == True: 
            return print('No hay registros')
        for v in ventas.leerVentas():
            print('Folio: ' +str(v.Id))
            print('Cliente: '+ v.Cliente.nombre)
            print('Estado: '+ v.estado)
            cesta = v.leerCesta()
            if cesta == True: return print('Lista Vacia')
            for c in cesta:
                print(str(c.Id) + "||" + c.nombre + "||" + str(c.precio)+ "||" + str(c.cantidad))
            print('Total: ' + str(v.total))
            print('Efectivo: ' + str(v.efectivo))
            print('Cambio: ' + str(v.cambio))
            print('--------------------------------------------------------------')
    
    def devVenta(self):
        v = ventas.buscarVenta(int(input('Ingresa el folio de la venta:\n')))
        v.devolucion()