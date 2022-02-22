import os
from Interfaces.InterfaceCliente import *
from Modelos.Lista import *
from Interfaces.Interface import *
from Modelos.Venta import *
from Modelos.Lista import *
from Interfaces.InterfaceProducto import *

cliente = InterfaceCliente().listaClientes
productos = InterfaceProducto().listaProductos
ventas = Lista()

class InterfaceVentas(Interface):
    def añadir(self):
        client = cliente.buscarElemento(
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
                elif opc == '0':
                    opc = 0
                else:
                    pass
                input()

    def leer(self):
        if ventas.leerElementos() == True: 
            return print('No hay registros')
        for v in ventas.leerElementos():
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
        v = ventas.buscarElementoId(int(input('Ingresa el folio de la venta:\n')))
        v.devolucion()

    def eliminar(self):
        pass
    def actualizar(self):
        pass