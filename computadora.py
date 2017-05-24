# -*- coding: utf-8 -*-
"""Éste es el módulo que contiene los algoritmos de análisis de jugada"""
from tablero import Tablero
class Computadora:
    """Genera jugadas en base al análisis del tablero."""
    combinaciones_ganadoras = Tablero.combinaciones_ganadoras
    def __init__(self, ficha):
        """inicializa el jugador de la CPU"""
        self.ficha = ficha

    def jugar(self, tablero):
        """analiza el tablero y retorna una jugada"""

    def buscar_victoria(self, tablero):
        """test"""


    def piedad(self, tablero):
        """cambia el modo de juego durante una partida"""
        pass

class Jugador:
    """Jugador fisico, tiene datos del jugador para el registro"""

    def __init__(self, nombre, ficha):
        """asigna el símbolo (X ó O) y un nombre para el."""
        self.nombre = nombre
        self.ficha = ficha

    def jugar(self):
        """jugar"""
        pass
