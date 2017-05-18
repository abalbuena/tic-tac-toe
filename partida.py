"""Módulo de controladores de partida."""
from computadora import Computadora

class Partida:
    """Controla la interacción de Jugador y Computadora durante una partida."""

    def __init__(self, tablero, jugador1, jugador2):
        """Inicia una partida"""
        self.tablero = tablero
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def alternar_turno(self):
        """returna el jugador que debe jugar"""
        pass

class PartidaUnJugador(Partida):
    """Controlador de partida para un jugador"""

    def __init__(self, tablero, jugador1):
        """Ïnicializa una partida para un jugador"""
        super().__init__(tablero, jugador1, Computadora())
    
    def alternar_turno(self):
        """intercala los turnos entre los jugadores"""
        pass