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
    def mostrar_tablero(self, tablero):
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

    def registrar_jugador(self, opciones_fichas):
        """Solicita al usuario un nobre para registrar en el historial."""
        datos_jugador = {}
        datos_jugador["nombre"] = input("Ingresá tu nombre: ")
        if not datos_jugador["nombre"]:
            datos_jugador.nombre = "anónimo"

        print("Seleccioná tu ficha: ")
        opciones = InterfazLineaComando.generar_opciones(opciones_fichas)
        self.print_opciones(opciones)
        ficha_seleccionada = self.solicitar_opcion(opciones_fichas)
        datos_jugador["ficha"] = ficha_seleccionada
        return datos_jugador

    def mostrar_tablero(self, tablero):
        """muestra el estado del tablero"""
        print(str(tablero))

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
                casilla = int(input("Seleccioná la casilla a marcar: "))
                if casilla in range(0, 9):
                    return casilla
                else:
                    print("seleccioná una casilla entre 0 y 9")
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
