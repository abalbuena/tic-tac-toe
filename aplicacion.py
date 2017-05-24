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

        self.interfaz.menu_principal(self.opciones_menu_principal,
                                     manejar_opcion_menu_princial)

    def partida_un_jugador(self):
        """Inicializa una partida para un jugador"""
        self.partida = Partida(self.interfaz)
        self.partida.iniciar_partida()
        print("partida de un jugador")

    def partida_dos_jugadores(self):
        """inicializa una partida para dos jugadores"""
        print("partida para dos jugadores")

    def historial(self):
        """obtiene el historial de partidas recientes"""
        print("opción historial")

if __name__ == "__main__":
    app = Application()
