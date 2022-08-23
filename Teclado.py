from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contadorTeclados = 0

    @classmethod
    def aumentarContador(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._idTeclado = Teclado.aumentarContador()

    def __str__(self):
        return f"Teclado[Id de teclado: {self._idTeclado}, {super().__str__()}]"

if __name__ == "__main__":
    teclado = Teclado("USB", "IQual")
    print(teclado)
