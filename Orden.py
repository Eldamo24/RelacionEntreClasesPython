from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:

    contadorOrdenes = 0

    @classmethod
    def aumentarContador(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self, computadoras):
        self._idOrden = Orden.aumentarContador()
        self._computadoras = list(computadoras)

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def __str__(self):
        compuString = ""
        for pc in self._computadoras:
            compuString += pc.__str__()
        return f"Orden[ID: {self._idOrden}\n\t{compuString}]"

if __name__ == "__main__":
    monitor = Monitor("HP", 24)
    teclado = Teclado("USB", "IQual")
    raton = Raton("USB", "Logitech")
    pc = Computadora("Damo", monitor, teclado, raton)
    monitor = Monitor("Samsung", 27)
    teclado = Teclado("USB", "Logitech")
    raton = Raton("USB", "Redragon")
    pc2 = Computadora("Demian", monitor, teclado, raton)
    computadoras = [pc, pc2]
    orden = Orden(computadoras)
    orden2 = Orden(computadoras)
    print(orden)
    print(orden2)