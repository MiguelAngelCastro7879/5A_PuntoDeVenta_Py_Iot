
class Producto:
    nombre = ""
    Id = 0
    precio:float = 0.00
    cantidad:float = 0
    def __init__(self, nombre, precio, cantidad):
        self.Id = id(self)
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad