from genericpath import exists
import json
import os


class archivosJSON:
    def __init__(self) -> None:
        pass
    def añadirProducto(self, prod):
        if os.path.exists('productos.json'):
            archivoProductos = open("productos.json", "a")
            archivoProductos.write(",")
        else:
            archivoProductos = open("productos.json", "a")
        p = {"Id": prod.Id, "nombre": prod.nombre,"precio": prod.precio,"cantidad": prod.cantidad}
        archivoProductos.write(json.dumps(p, indent=4))
        archivoProductos.close()
        pass
    def añadirCliente(self, clnt):
        if os.path.exists('clientes.json'):
            archivoClientes = open("clientes.json", "a")
            archivoClientes.write(",")
        else:
            archivoClientes = open("clientes.json", "a")
        c = {"Id": clnt.Id, "nombre": clnt.nombre}
        archivoClientes.write(json.dumps(c, indent=4))
        archivoClientes.close()
        pass
    def añadirVenta(self, vnt):
        data = {}
        data['productos'] = []
        for prod in vnt.ListaProductos.leerProductos():
            data['productos'].append({"Id": prod.Id, "nombre": prod.nombre,"precio": prod.precio,"cantidad": prod.cantidad})        

        
        if os.path.exists('registroVentas.json'):
            archivoClientes = open("registroVentas.json", "a")
            archivoClientes.write(",")
        else:
            archivoVentas = open("registroVentas.json", "a")
        c = {"Id": vnt.Id, 
        "Cliente": {
            "Id": vnt.Cliente.Id, "nombre": vnt.Cliente.nombre
            }, 
        "estado": vnt.estado, 
        "total": vnt.total,
        "efectivo": vnt.efectivo,
        "cambio": vnt.cambio,
        "Lista Productos": data['productos'],}
        archivoVentas.write(json.dumps(c, indent=4))
        archivoVentas.close()
        pass