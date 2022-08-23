class Monitor():
    contadorMonitores = 0

    @classmethod
    def aumentarContador(cls):
        cls.contadorMonitores += 1
        return cls.contadorMonitores

    def __init__(self, marca, tamanio):
        self._idMonitor = Monitor.aumentarContador()
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    @property
    def idMonitor(self):
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    def __str__(self):
        return f"Monitor[Id: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamanio}]"

if __name__ == "__main__":
    monitor = Monitor("HP", 24)
    print(monitor)