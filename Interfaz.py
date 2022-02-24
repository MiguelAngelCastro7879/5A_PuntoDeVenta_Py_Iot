from colorama import Style
import os
from Acciones import *
from Interfaces.InterfaceProducto import *



class Interfaz:
    productos = InterfaceProducto()

    def __init__(self):
        productos.importarDatos()
        self.menu()
    def menu(self):
        opc = ''
        while opc != '0':
            os.system('cls')
            print(Style.RESET_ALL + Style.BRIGHT +f"  MENU PRINCIPAL\
                \n//////////////////\
                \n[1]Productos\
                \n[2]Clientes\
                \n[3]Ventas\
                \n[0]MENU ANTERIOR")
            opc = input()
            if opc == '1' or opc == '2' or opc == '3':
                self.submenu(opc)
            elif opc != '0':
                print("OPCION NO VALIDA")
                input()
            else:
                pass
    def submenu(self, opcion):
        palabra = ''
        if opcion == '1':palabra = 'Producto'
        elif opcion == '2':palabra = 'Cliente'
        elif opcion == '3':palabra = 'Venta'
        opc = ''
        while opc != '0':
            os.system('cls')
            if opcion == '1' or opcion=='2':
                print(Style.RESET_ALL +Style.BRIGHT + f"  Menu De "+ palabra+" \
                        \n//////////////////\
                        \n[1]Crear "+ palabra+"\
                        \n[2]Leer "+ palabra+"s\
                        \n[3]Eliminar "+ palabra+"\
                        \n[4]Actualizar "+ palabra+"\
                        \n[0]MENU ANTERIOR")
            else:
                print(Style.RESET_ALL +Style.BRIGHT + f"  Menu De "+ palabra+"\
                        \n//////////////////\
                        \n[1]Crear "+ palabra+"\
                        \n[2]Leer "+ palabra+"s\
                        \n[3]Realizar Devolucion\
                        \n[0]MENU ANTERIOR")
            opc = input()
            Acciones(opcion, opc)