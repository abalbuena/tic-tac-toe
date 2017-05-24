"""Módulo de controladores de partida."""
from itertools import cycle
from computadora import Jugador, Computadora
from tablero import Tablero

class Partida():
    """Controlador de partida para un jugador"""
    fichas = ({'codigo': "0", 'descripcion': "O"},
              {'codigo': "1", 'descripcion': "X"})

    opciones_inicio = ({'codigo': "0", 'descripcion': "O"},
                       {'codigo': "1", 'descripcion': "X"})

    def __init__(self, interfaz):
        """Inicializa una partida para un jugador"""
        self.interfaz = interfaz
        datos_jugador = self.interfaz.registrar_jugador(self.fichas)
        jugador = Jugador(datos_jugador["nombre"], datos_jugador["ficha"])
        self.tablero = Tablero()
        #inicializa un ciclo entre computadora y jugador.
        self.jugadores = cycle((jugador, computadora))
    
    def iniciar_partida(self):
        jugador = self.alternar_turno()
        if type(jugador) is Jugador:
            self.interfaz.
        elif type(jugador) is Computadora:
            jugador.jugar(self.tablero)

    def alternar_turno(self):
        """intercala los turnos entre los jugadores"""
        yield next(self.jugadores)
