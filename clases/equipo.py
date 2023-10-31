from .clases_abstractas.ciclista import Ciclista


class Equipo:
    def __init__(self, nombre: str, pais: str):
        self.__nombre = nombre
        self.__pais = pais
        self.__totalTiempo = 0
        self.__ciclistas: list[Ciclista] = []

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def getPais(self):
        return self.__pais

    def setPais(self, pais: str):
        self.__pais = pais

    def anadirCiclista(self, ciclista: Ciclista):
        self.__ciclistas.append(ciclista)

    def listarEquipo(self):
        for ciclista in self.__ciclistas:
            print("=================================================================")
            ciclista.imprimir()
            print("=================================================================")

    def calcularTotalTiempo(self):
        if len(self.__ciclistas) > 0:
            for ciclista in self.__ciclistas:
                self.__totalTiempo += ciclista.getTiempoAcumulado()
        return self.__totalTiempo

    def buscarCiclista(self, valor: str, parametro: str = "nombre"):
        if parametro == "nombre":
            ciclista = [ccli for ccli in self.__ciclistas if ccli.getNombre() == valor]
            if len(ciclista) > 0:
                ciclista[0].imprimir()
            else:
                print("No se encontro un ciclista con ese nombre")
        elif parametro == "identificador":
            ciclista = [ccli for ccli in self.__ciclistas if ccli.getIdentificador() == int(valor)]
            if len(ciclista) > 0:
                ciclista[0].imprimir()
            else:
                print("No se encontro un ciclista con ese identificador")
        else:
            print("Esa propiedad no existe, solo es permitido nombre e identificador")

    def imprimir(self):
        print(f"el nombre de el equipo es: {self.getNombre()}\n"
              f"El pais de el equipo es: {self.getPais()}\n"
              f"El tiempo total de el equipo es: {self.calcularTotalTiempo()}")
