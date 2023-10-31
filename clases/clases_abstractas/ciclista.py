from abc import ABC, abstractmethod


class Ciclista(ABC):
    @abstractmethod
    def __init__(self, identificador: int, nombre: str, tiempoAcumulado: float):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempoAcumulado = tiempoAcumulado

    @abstractmethod
    def imprimirTipo(self):
        pass

    def getIdentificador(self):
        return self.__identificador

    def setIdentificador(self, identificador: int):
        self.__identificador = identificador

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def getTiempoAcumulado(self):
        return self.__tiempoAcumulado

    def setTiempoAcumulado(self, tiempoAcumulado: int):
        self.__tiempoAcumulado = tiempoAcumulado

    def imprimir(self):
        print(f"El nombre del ciclista es {self.getNombre()}\n"
              f"Su identificador es: {self.getIdentificador()}\n"
              f"El tiempo acumulado es: {self.getTiempoAcumulado()}")