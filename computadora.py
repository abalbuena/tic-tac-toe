# -*- coding: utf-8 -*-
"""Éste es el módulo que contiene los algoritmos de análisis de jugada"""
class Computadora:
    """Genera jugadas en base al análisis del tablero."""
    def __init__(self):
        """inicializa el jugador de la CPU"""
        pass

    def jugar(self, tablero):
        """analiza el tablero y retorna una jugada"""
        pass

    def piedad(self, tablero):
        """cambia el modo de juego durante una partida"""
        pass

class Jugador:
    """Jugador fisico, tiene datos del jugador para el registro"""

    def __init__(self, nombre, ficha):
        """asigna el símbolo (X ó O) y un nombre para el."""
        self.nombre = nombre
        self.ficha = ficha
