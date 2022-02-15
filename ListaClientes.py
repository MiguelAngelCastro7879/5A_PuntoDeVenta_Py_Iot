from Lista import * 
from archivosJSON import *

class ListaClientes(Lista):
    def __init__(self):
        super().__init__()

    def agregarCliente(self, Cliente):
        self.agregarElemento(Cliente)
        ajs = archivosJSON()
        ajs.añadirCliente(Cliente)

    def eliminarCliente(self, clienteNombre):
        p = self.buscarCliente(clienteNombre)
        if p != False and p !=True:
            self.eliminarElemento(self.buscarCliente(clienteNombre))    
        else: return False

    def leerClientes(self):
        return self.leerElementos()

    def buscarCliente(self, clienteNombre):
        if self.leerElementos() == True:
            return True
        for elemento in self.leerElementos():
            if elemento.nombre == clienteNombre:
                return elemento
        return False