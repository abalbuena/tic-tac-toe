# -*- coding: utf-8 -*-
"""Éste es el módulo que contiene los algoritmos de análisis de jugada"""

class Computadora:
    """Genera jugadas en base al análisis del tablero."""

    def __init__(self, ficha):
        """inicializa el jugador de la CPU"""
        self.ficha = ficha

    def jugar(self, tablero):
        """analiza el tablero y retorna una jugada"""
        disponibles = tablero.casillas_disponibles()
        casilla_seleccionada = disponibles[0]
        print(str(casilla_seleccionada.indice - 1))
        return casilla_seleccionada.indice - 1

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
