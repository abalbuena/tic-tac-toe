"""Modulo de interfaz"""
from abc import ABC, abstractmethod

class Interfaz(ABC):
    """Esquema para las intefaces de la aplicación"""

    @abstractmethod
    def menu_principal(self, opciones, callback):
        """Menú principal de la aplicación"""
        pass
    @abstractmethod
    def registrar_jugador(self, opciones_fichas):
        """Permite al jugador ingresar sus datos."""
        pass

    @abstractmethod
    def mostrar_tablero(self):
        """Interfaz del juego"""
        pass

class InterfazLineaComando(Interfaz):
    """Interfaz por línea de comandos"""

    saludo_inicial = ("TATETI Python \n")

    def __init__(self):
        print("Interfaz inicializada")

    def menu_principal(self, opciones, callback):
        """imprime el menú principal y recibe la opción seleccionada"""
        print(self.saludo_inicial)
        opciones_menu = InterfazLineaComando.ordenar_opciones(opciones)

        for opcion in opciones_menu:
            print(opcion + "\n") #imprime la opción más un saldo de línea.

        while True:
            try:
                opcion_index = int(input("Seleccioná una opción: "))
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

    def registrar_jugador(self, opciones_fichas):
        """Solicita al usuario un nobre para registrar en el historial."""
        datos_jugador = {}
        datos_jugador["nombre"] = input("Ingresá tu nombre: ")
        if not datos_jugador["nombre"]:
            datos_jugador.nombre = "anónimo"

        print("Seleccioná tu ficha: ")
        opciones_texto = InterfazLineaComando.ordenar_opciones(opciones_fichas)
        self.print_opciones(opciones_texto)
        ficha_seleccionada = self.solicitar_opcion(opciones_fichas)
        datos_jugador["ficha"] = ficha_seleccionada
        return datos_jugador

    def mostrar_tablero(self):
        """muestra el estado del tablero"""
        pass

    def solicitar_opcion(self, opciones):
        """método genérico que solicita al usuario que seleccione una opción"""
        while True:
            try:
                opcion_index = int(input("Seleccioná una opción: "))
                try:
                    opcion_seleccionada = opciones[opcion_index]
                    return opcion_seleccionada
                except IndexError:
                    print("el valor ingresado no corresponde a ninguna opción")
                    opcion_index = int(input("seleccioná una opción: "))
                    continue
            except ValueError:
                print("ingresá un valor numérico!")
                continue

    @staticmethod
    def ordenar_opciones(opciones):
        """genera una lista tipo menú de opciones"""
        opciones_string = []
        for i, opcion in enumerate(opciones):
            opciones_string.append("{0}) {1}".format(i, opcion['descripcion']))

        return opciones_string

    @staticmethod
    def print_opciones(opciones):
        """método genérico para imprimir opciones en pantalla"""
        for opcion in opciones:
            print(opcion + "\n") #imprime la opción más un saldo de línea.
    
    def pedir_jugada(self, nombre):
        print("Seleccioná la casilla a marcar: ")