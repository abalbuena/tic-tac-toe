# -*- coding: utf-8 -*-

"""Inicia la aplicación"""
from interfaz import InterfazLineaComando
from partida import Partida

class Application:
    """Maneja los controladores de partida, BD, etc."""

    opciones_menu_principal = ("partida de un jugador",
                               "partida de dos jugadores",
                               "historial")

    def __init__(self):
        """crea el tablero, y los jugadores, y el controlador de partida"""
        self.interfaz = InterfazLineaComando()

        def manejar_opcion_menu_princial(opcion):
            """Maneja la opción seleccionada por el usuario en el menú
               principal"""

            if self.opciones_menu_principal.index(opcion) == 0:
                self.partida_un_jugador()
            elif self.opciones_menu_principal.index(opcion) == 1:
                self.partida_dos_jugadores()
        self.interfaz.menu_principal(self.opciones_menu_principal,
                                     manejar_opcion_menu_princial)

    def partida_un_jugador(self):
        """Inicializa una partida para un jugador"""
        self.partida = Partida(self.interfaz, 1)
        self.partida.iniciar_partida()

    def partida_dos_jugadores(self):
        """inicializa una partida para dos jugadores"""
        self.partida = Partida(self.interfaz, 2)
        self.partida.iniciar_partida()

    def historial(self):
        """obtiene el historial de partidas recientes"""
        print("opción historial")

    def salir(self):
        """
        Cierra la aplicación.
        """
        quit()
if __name__ == "__main__":
    Application()
