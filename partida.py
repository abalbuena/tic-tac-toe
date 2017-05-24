"""Módulo de controladores de partida."""
from itertools import cycle
from computadora import Jugador, Computadora
from tablero import Tablero, Jugada

class Partida():
    """Controlador de partida para un jugador"""
    fichas = ["X", "O"]

    def __init__(self, interfaz):
        """Inicializa una partida para un jugador"""
        self.interfaz = interfaz
        datos_jugador = self.interfaz.registrar_jugador(self.fichas)
        jugador = Jugador(datos_jugador["nombre"], datos_jugador["ficha"])

        if self.fichas.index(jugador.ficha) == 0:
            ficha_computadora = self.fichas[1]
        else:
            ficha_computadora = self.fichas[0]
        computadora = Computadora(ficha_computadora)
        self.tablero = Tablero()
        #inicializa un ciclo entre computadora y jugador.
        self.jugadores = (jugador, computadora)
        self.turnos = cycle(self.jugadores)

    def iniciar_partida(self):
        """inicializa la partida"""
        partida_terminada = False
        while not partida_terminada:
            jugador = self.alternar_turno()
            print(self.tablero)
            if isinstance(jugador, Jugador):
                casilla = self.interfaz.pedir_jugada()
                jugada = Jugada(casilla, jugador.ficha)
                self.tablero.marcar_casilla(jugada)
                partida_terminada = self.tablero.buscar_ganador(jugada)
            elif isinstance(jugador, Computadora):
                print("turno de la computadora")

            self.interfaz.mostrar_tablero(self.tablero)

    def alternar_turno(self):
        """intercala los turnos entre los jugadores"""
        return next(self.turnos)
