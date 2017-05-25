"""Modulo de interfaz"""
from abc import ABC, abstractmethod
import os

class Interfaz(ABC):
    """Esquema para las intefaces de la aplicación"""

    @abstractmethod
    def menu_principal(self, opciones, callback):
        """Menú principal de la aplicación"""
        pass
    @abstractmethod
    def registrar_jugador(self):
        """implementar para permitir ingresar un nombre para los registros."""
        pass

    @abstractmethod
    def seleccionar_ficha(self, opciones_fichas):
        """implementar para permitir al usuario seleccionar la ficha"""
    @abstractmethod
    def mostrar_tablero(self, tablero):
        """Interfaz del juego"""
        pass
    @abstractmethod
    def notificacion(self, mensaje, limpiar_pantalla=False):
        """implementar para notificar errores al usuario."""

class InterfazLineaComando(Interfaz):
    """Interfaz por línea de comandos"""

    saludo_inicial = ("TATETI Python \n")
    fila = lambda fila, columna: '\033[' + str(fila) + str(columna) + 'H'

    def __init__(self):
        print("Interfaz inicializada")

    def menu_principal(self, opciones, callback):
        """imprime el menú principal y recibe la opción seleccionada"""
        print(self.saludo_inicial)
        opciones_menu = InterfazLineaComando.generar_opciones(opciones)

        for opcion in opciones_menu:
            print(str(opcion) + "\n") #imprime la opción más un saldo de línea.

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

    def registrar_jugador(self):
        """Solicita al usuario un nobre para registrar en el historial."""
        nombre = input("Ingresá tu nombre: ")
        return nombre

    def seleccionar_ficha(self, opciones_fichas):
        """presenta las fichas para que el usuario elija"""
        print("Seleccioná tu ficha: ")
        opciones = InterfazLineaComando.generar_opciones(opciones_fichas)
        self.print_opciones(opciones)
        ficha_seleccionada = self.solicitar_opcion(opciones_fichas)
        return ficha_seleccionada

    def mostrar_tablero(self, tablero):
        """muestra el estado del tablero"""
        filas_pantalla = [InterfazLineaComando.fila(x, 5) for x in range(3, 12)]
        print('\n')
        print('\033[2;4H  TEST')

        print(filas_pantalla[0] + "        |       |         ")
        print(filas_pantalla[1] + "    {0}   |   {1}   |   {2}   ".format(
            tablero.tabla(1),
            tablero.tabla(2),
            tablero.tabla(3)))

        print(filas_pantalla[2] + "________|_______|________")
        print(filas_pantalla[3] + "        |       |        ")
        print(filas_pantalla[4] + "    {3}   |   {4}   |   {5}   ".format(
            tablero.tabla(4),
            tablero.tabla(5),
            tablero.tabla(6)))
        print(filas_pantalla[5] + "________|_______|_______")
        print(filas_pantalla[6] + "        |       |       ")
        print(filas_pantalla[7] + "    {6}   |   {7}   |   {8}   ".format(
            tablero.tabla(7),
            tablero.tabla(8),
            tablero.tabla(9)))
        print(filas_pantalla[8] + "        |       |       ")

    def notificacion(self, mensaje, limpiar_pantalla=False):
        """imprime el mensaje"""
        if limpiar_pantalla:
            self.limpiar_pantalla()
        print(mensaje)

    def limpiar_pantalla(self):
        """limpia la pantalla"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def solicitar_opcion(self, opciones):
        """método genérico que solicita al usuario que seleccione una opción"""
        while True:
            try:
                opcion_index = int(input("\033[12;5HSeleccioná una opción: "))
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
    def generar_opciones(opciones):
        """genera una lista tipo menú de opciones"""
        opciones_interfaz = []
        for i, opcion in enumerate(opciones):
            opcion_interfaz = OpcionInterfaz(i, str(opcion), opcion)
            opciones_interfaz.append(opcion_interfaz)

        return opciones_interfaz

    @staticmethod
    def print_opciones(opciones):
        """método genérico para imprimir opciones en pantalla"""
        for opcion in opciones:
            print(str(opcion) + "\n") #imprime la opción más un salto de línea

    def pedir_jugada(self):
        """recibe la jugada del usuario"""
        while True:
            try:
                casilla = int(input("\n Seleccioná la casilla a marcar: "))
                if casilla in range(1, 10):
                    return casilla
                else:
                    print("seleccioná una casilla entre 1 y 9")
                    continue
            except ValueError:
                print("ingresá un valor numérico")
                continue

class OpcionInterfaz:
    """estructura genérica para representar una opción en la interfaz"""
    def __init__(self, indice, descripcion, valor):
        """
            genera una opcion para la interfaz
            indice : numero que corresponde a la opcion
            descripcion : descripcion del valor que representa
            valor : valor que representa.
        """
        self.indice = indice
        self.descripcion = descripcion
        self.valor = valor

    def __str__(self):
        return "{0} - {1}".format(self.indice, self.descripcion)
