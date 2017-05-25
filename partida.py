"""Módulo de controladores de partida."""
from itertools import cycle
from computadora import Jugador, Computadora
from tablero import Tablero, Jugada

class Partida():
    """Controlador de partida para un jugador"""
    fichas = ["X", "O"]
    tipos_partida = {"jugador_vs_computadora" : 0,
                     "jugador_vs_jugador": 1}

    def __init__(self, interfaz, jugadores):
        """Inicializa una partida para un jugador"""
        self.interfaz = interfaz
        nombre_jugador = self.interfaz.registrar_jugador()
        ficha_jugador = self.interfaz.seleccionar_ficha(self.fichas)
        jugador = Jugador(nombre_jugador, ficha_jugador)

        if self.fichas.index(jugador.ficha) == 0:
            ficha_oponente = self.fichas[1]
        else:
            ficha_oponente = self.fichas[0]

        if jugadores < 2:
            jugador2 = Computadora(ficha_oponente)
        else:
            nombre_jugador = self.interfaz.registrar_jugador()
            jugador2 = Jugador(nombre_jugador, ficha_oponente)

        self.tablero = Tablero()
        #inicializa un ciclo entre computadora y jugador.
        self.jugadores = (jugador, jugador2)
        self.turnos = cycle(self.jugadores)

    def iniciar_partida(self):
        """inicializa la partida"""
        partida_terminada = False
        jugador = self.alternar_turno()
        while not partida_terminada:
            jugador = self.alternar_turno()
            print(self.tablero)
            if isinstance(jugador, Jugador):
                casilla = self.interfaz.pedir_jugada()
                jugada = Jugada(casilla, jugador.ficha)
                self.tablero.marcar_casilla(jugada)
                partida_terminada = self.tablero.buscar_ganador(jugada)
            elif isinstance(jugador, Computadora):
                casilla = jugador.jugar(self.tablero)
                jugada = Jugada(casilla, jugador.ficha)
                self.tablero.marcar_casilla(jugada)
                partida_terminada = self.tablero.buscar_ganador(jugada)

            self.interfaz.mostrar_tablero(self.tablero)

        self.interfaz.mostrar_tablero(self.tablero)
        print("partida terminada! ganador {0}".format(jugador.ficha))

    def alternar_turno(self):
        """intercala los turnos entre los jugadores"""
        return next(self.turnos)
