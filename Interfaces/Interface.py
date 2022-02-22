from abc import abstractmethod
from abc import ABCMeta

class Interface(metaclass=ABCMeta):
    @abstractmethod
    def añadir(self):
        pass
    @abstractmethod
    def leer(self):
        pass
    @abstractmethod
    def eliminar(self):
        pass
    @abstractmethod
    def actualizar(self):
        pass
    