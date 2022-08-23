from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contadorRatones = 0

    @classmethod
    def aumentarContador(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._idRaton = Raton.aumentarContador()

    def __str__(self):
        return f"Raton[Id de raton: {self._idRaton}, {super().__str__()}]"

if __name__ == "__main__":
    raton = Raton("USB", "Logitech")
    print(raton)