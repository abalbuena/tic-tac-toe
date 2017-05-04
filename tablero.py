class Jugador:
    """Interactua con el tablero"""
    nombre = "anónimo"
    ficha = "X"

    def __init__(self, nombre, ficha):
        """asigna el símbolo (X ó O) y un nombre para el historial."""
        self.nombre = nombre
        self.ficha = ficha

    def jugar(self, tablero):
        """analiza el tablero y retorna la jugada."""
        #TODO:analizar el tablero: y retornar jugada.

#combinaciones ganadoras
class Tablero:
    """Controla las casillas del juego"""
    tabla = []
    combinaciones_ganadoras = (
        [[(x, y) for y in range(3)] for x in range(3)] + # combinaciones horizontales
        [[(x, y) for x in range(3)] for y in range(3)] + # combinaciones verticales
        [[(d, d) for d in range(3)]] + # diagonal principal
        [[(2-d, d) for d in range(3)]] # diagonal secundaria.
    )

    def __init__(self):
        """carga el tablero"""
        self.generar_tablero()
        #TODO: hacer algo;
    
    def generar_tablero(self):
        """genera un nuevo tablero"""
        for fila in range(3):
            self.tabla.append([])
        for column in range(3):
            self.tabla[fila].append('-')

        return self.tabla
    
    def buscar_ganador(self, jugada):
        """busca un ganador según su ficha"""
        combinaciones_posibles = self.combinaciones_para_jugada(jugada)
        for combinacion_ganadora in combinaciones_posibles:
            #obtiene las combinaciones ganadores para la casilla seleccionada.
            valores = [self.tabla[x][y] for (x, y) in combinacion_ganadora]
            if len(set(valores)) == 1:
                return True
        
        return False

    def combinaciones_para_jugada(self, jugada):
        """obtiene las combinaciones ganadoras para una determinada jugada"""
        combinaciones = []
        for item in self.combinaciones_ganadoras:
            if jugada in item:
                combinaciones.append(item)
        
        return combinaciones

class Application: 
    """Maneja los controladores de partida, BD, etc."""

    def iniciar(self):
        """crea el tablero, y los jugadores, y el controlador de partida"""
        tablero = Tablero()
        tablero.tabla = [["X", "X", "."],["O", "O", "X"],["O", "O", "."]]
        hay_ganador = tablero.buscar_ganador((1, 2))
        print(hay_ganador)

class PartidaController:
    """Controla la interacción de jugador y tablero durante una partida."""

    def __init__(self, jablero, jugadores):
        """"""
        self.tablero = Tablero()
        self.jugadores = jugadores

if __name__ == "__main__":
    application = Application()
    application.iniciar()