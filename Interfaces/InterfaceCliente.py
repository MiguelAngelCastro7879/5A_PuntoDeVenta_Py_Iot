
from Modelos.Lista import *
from Modelos.Cliente import *
from Interfaces.Interface import *
from archivosJSON import archivosJSON
json = archivosJSON()

class InterfaceCliente(Interface):
    listaClientes = Lista()
    def __init__(self) -> None:
        super().__init__()

    def añadir(self):
        self.listaClientes.agregarElemento(
            Cliente(
                input('Escribe el nombre del nuevo Cliente:\n'))) 
        json.escribirClientes(self.listaClientes)
    
    def leer(self):
        if self.listaClientes.leerElementos() == True:
            return print('Lista Vacia')
        for client in self.listaClientes.leerElementos():
            print(str(client.Id) + "||" + client.nombre )
    
    def eliminar(self):
        if self.listaClientes.leerElementos()== True:
            return print('Lista Vacia')
        c = self.listaClientes.eliminarElemento(input('Ingresa El nombre del Cliente a eliminar: '))
        if c == False:
            print('Elemento no encontrado')
        else:
            print('Cliente eliminado')
        json.escribirClientes(self.listaClientes)
    
    def actualizar(self):
        c = self.listaClientes.buscarElemento(
            input('Ingresa el nombre del cliente a actualizar: \n'))
        if c == True:
            print('Lista Vacia')
        elif c == False:
            print('Cliente no encontrado')
        else:
            c.nombre = input('Ingresa el nuevo nombre del Cliente:\n')
            print('Cliente:')
            print(str(c.Id) + "||" + c.nombre)
        json.escribirClientes(self.listaClientes)
   