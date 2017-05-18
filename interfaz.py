"""Modulo de interfaz"""
from abc import ABC, abstractmethod

class Interfaz(ABC):
    """Esquema para las intefaces de la aplicación"""

    @abstractmethod
    def menu_principal(self, opciones, callback):
        """Menú principal de la aplicación"""
        pass

    @abstractmethod
    def mostrar_tablero(self):
        """Interfaz del juego"""
        pass

class IntefazLineaComando(Interfaz):
    """Interfaz por línea de comandos"""

    saludo_inicial = ("TATETI Python \n")

    def __init__(self):
        print("Interfaz inicializada")

    def menu_principal(self, opciones, callback):
        """imprime el menú principal y recibe la opción seleccionada"""
        print(self.saludo_inicial)
        opciones_menu = self.ordenar_opciones(opciones)

        for opcion in opciones_menu:
            print(opcion + "\n") #imprime la opción más un saldo de línea.

        while True:
            try:
                opcion_index = int(input("Ingresá la opción: "))
                try:
                    opcion_seleccionada = opciones[opcion_index]
                    callback(opcion_seleccionada)
                    break
                except IndexError:
                    print("el valor ingresado no corresponde a ninguna opción")
                    opcion_index = int(input("seleccioná una opción: "))
                    continue
            except ValueError:
                print("ingresá un valor numérico!")
                continue

    def mostrar_tablero(self):
        """muestra el estado del tablero"""
        pass

    def ordenar_opciones(self, opciones):
        """genera una lista más amigable de las opciones del menú"""
        opciones_string = []
        for i, opcion in enumerate(opciones):
            opciones_string.append("{0}) {1}".format(i, opcion['descripcion']))

        return opciones_string
