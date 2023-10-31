from .clases_abstractas.ciclista import Ciclista


class Escalador(Ciclista):
    def __init__(self, identificador: int, nombre: str, aceleracionPromedio: float, gradoRampa: float, tiempoAcumulado: float):
        super().__init__(identificador, nombre, tiempoAcumulado)
        self.__aceleracionPromedio = aceleracionPromedio
        self.__gradoRampa = gradoRampa

    def getAceleracionPromedio(self):
        return self.__aceleracionPromedio

    def setAceleracionPromedio(self, aceleracionPromedio):
        self.__aceleracionPromedio = aceleracionPromedio

    def getGradoRampa(self):
        return self.__gradoRampa

    def setGradoRampa(self, gradoRampa):
        self.__gradoRampa = gradoRampa

    def imprimirTipo(self):
        print("El tipo de ciclista es escalador")

    def imprimir(self):
        self.imprimirTipo()
        print(f"El nombre del ciclista es {self.getNombre()}\n"
              f"Su identificador es: {self.getIdentificador()}\n"
              f"El tiempo acumulado es: {self.getTiempoAcumulado()}\n"
              f"La Aceleracion Promedio es: {self.getAceleracionPromedio()}\n"
              f"El grado de rampa es: {self.getGradoRampa()}")

