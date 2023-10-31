from .clases_abstractas.ciclista import Ciclista


class Velocista(Ciclista):
    def __init__(self, identificador: int, nombre: str, potenciaPromedio: float, velocidadPromedio: float,  tiempoAcumulado: float):
        super().__init__(identificador, nombre, tiempoAcumulado)
        self.__potenciaPromedio = potenciaPromedio
        self.__velocidadPromedio = velocidadPromedio

    def getPotenciaPromedio(self):
        return self.__potenciaPromedio

    def setPotenciaPromedio(self, potenciaPromedio):
        self.__potenciaPromedio = potenciaPromedio

    def getVelocidadPromedio(self):
        return self.__velocidadPromedio

    def setVelocidadPromedio(self, velocidadPromedio):
        self.__velocidadPromedio = velocidadPromedio

    def imprimirTipo(self):
        print(f"El tipo de ciclista es velocista")

    def imprimir(self):
        self.imprimirTipo()
        print(f"El nombre del ciclista es {self.getNombre()}\n"
              f"Su identificador es: {self.getIdentificador()}\n"
              f"El tiempo acumulado es: {self.getTiempoAcumulado()}\n"
              f"La velocidad promedio es : {self.getVelocidadPromedio()}")
