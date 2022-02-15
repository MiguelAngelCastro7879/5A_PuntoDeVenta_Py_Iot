class Lista:
    ListaElementos = ['']

    def __init__(self):
        self.ListaElementos = []
        
        # CREATE
    def agregarElemento(self, elm):
        self.ListaElementos.append(elm)

        # READ
    def leerElementos(self):
        if len(self.ListaElementos) == 0:
            return True
        return self.ListaElementos

        # UPDATE
    def actualizarElemento(self, elm, elmAct):
        actualizado = self.buscarElemento(elm)
        #Si actualizado es True significa que la lista está vacia
        #Si es false significa que no se encontró el elemento
        if actualizado != True and actualizado != False:
            self.ListaElementos[self.ListaElementos.index(actualizado)] = elmAct
        return actualizado

        # DELETE
    def eliminarElemento(self, elm):
        borrado = self.buscarElemento(elm)
        #Si borrado es True significa que la lista está vacia
        #Si es false significa que no se encontró el elemento
        if borrado != True and borrado != False:
            self.ListaElementos.remove(borrado)
        return borrado

    def buscarElemento(self, elm):
        if len(self.ListaElementos) == 0:
            return True
        else:
            for elemento in self.ListaElementos:
                if elemento == elm:
                    return elemento
            return False
