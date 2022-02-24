from genericpath import exists
import json
pr = "JSON/Productos.json"
vn = "JSON/Ventas.json"
cl = "JSON/Clientes.json"

class archivosJSON:
    def __init__(self):
        pass
    def escribirProductos(self, productos):
        f = open(pr, "w")
        data = {}
        data['productos'] = []
        for prod in productos.leerElementos():
            data['productos'].append({"Id": prod.Id, "nombre": prod.nombre,"precio": prod.precio,"cantidad": prod.cantidad})  
        f.write(json.dumps(data, indent=4))
        f.close()
        pass
    def escribirClientes(self, clientes):
        f = open(cl, "w")
        data = {}
        data['clientes'] = []
        for prod in clientes.leerElementos():
            data['clientes'].append({"Id": prod.Id, "nombre": prod.nombre})  
        f.write(json.dumps(data, indent=4))
        f.close()
        pass
    def escribirVentas(self, ventas):
        f = open(vn, "w")
        data = {}
        data['ventas'] = []
        for venta in ventas.leerElementos():
            
            p = {}
            p['productos'] = []
            
            for prod in venta.ListaProductos.leerElementos():
                p['productos'].append({"Id": prod.Id, "nombre": prod.nombre,"precio": prod.precio,"cantidad": prod.cantidad})  
            data['ventas'].append(
                                    {"Id": venta.Id, 
                                        "Cliente": {
                                                "Id": venta.Cliente.Id, 
                                                "nombre": venta.Cliente.nombre
                                            }, 
                                        "estado": venta.estado, 
                                        "total": venta.total,
                                        "efectivo": venta.efectivo,
                                        "cambio": venta.cambio,
                                        "Lista de productos": p['productos'],}) 
        f.write(json.dumps(data, indent=4))
        f.close()
        pass
    
    def leerProductos(self):
        f = open(pr, "r")
        data = json.load(f)
        f.close()
        return data