from .clases_abstractas.ciclista import Ciclista

class Contrarrelojista(Ciclista):
    def __init__(self, identificador: int, nombre: str, velocidadMaxima: float, tiempoAcumulado: float):
        super().__init__(identificador, nombre, tiempoAcumulado)
        self.__velocidadMaxima = velocidadMaxima

    def getVelocidadMaxima(self):
        return self.__velocidadMaxima

    def setVelocidadMaxima(self, velocidadMaxima):
        self.__velocidadMaxima = velocidadMaxima

    def imprimirTipo(self):
        print("El tipo de ciclista es: contrarrelojista")

    def imprimir(self):
        self.imprimirTipo()
        print(f"El nombre del ciclista es {self.getNombre()}\n"
              f"Su identificador es: {self.getIdentificador()}\n"
              f"El tiempo acumulado es: {self.getTiempoAcumulado()}\n"
              f"La velocidad maxima es: {self.getVelocidadMaxima()}")