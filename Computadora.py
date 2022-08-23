from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora():

    contadorComputadoras = 0

    @classmethod
    def aumentarContador(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._idComputadora = Computadora.aumentarContador()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def idComputadora(self):
        return self._idComputadora

    @idComputadora.setter
    def idComputadora(self, idComputadora):
        self._idComputadora = idComputadora

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f"\n\tComputadora: ID: {self._idComputadora}, Nombre: {self._nombre} \n\t{self._monitor} \n\t{self._teclado} \n\t{self._raton}"

if __name__ == "__main__":
    monitor = Monitor("HP", 24)
    teclado = Teclado("USB", "IQual")
    raton = Raton("USB", "Logitech")
    pc = Computadora("Damo", monitor, teclado, raton)
    print(pc)