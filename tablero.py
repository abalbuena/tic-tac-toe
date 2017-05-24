#combinaciones ganadoras
class Tablero:
    """gestiona las casillas del juego"""
    tabla = []

    """genera una tupla con las combinaciones ganadoras (listas de casillas)"""
    combinaciones_ganadoras = (
        [[(x, y) for y in range(3)] for x in range(3)] + # combinaciones horizontales
        [[(x, y) for x in range(3)] for y in range(3)] + # combinaciones verticales
        [[(d, d) for d in range(3)]] + # diagonal principal
        [[(2-d, d) for d in range(3)]] # diagonal secundaria.
    )

    def __init__(self):
        """carga el tablero"""
        self.generar_tablero()

    def generar_tablero(self):
        """genera un nuevo tablero"""
        for fila in range(3):
            self.tabla.append([])
            for index in range(3):
                self.tabla[fila].append(index)

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

    def __str__(self):
        tablero_string = ("      |     |     \n"
                          "   0  |  1  |  2  \n"
                          "______|_____|_____\n"
                          "      |     |     \n"
                          "   3  |  4  |  5  \n"
                          "______|_____|_____\n"
                          "      |     |     \n"
                          "   6  |  7  |  8  \n"
                          "      |     |     ")

        tablero_string.format(self.tabla[0][0], self.tabla[0][1], self.tabla[0][2],
                              self.tabla[1][0], self.tabla[1][1], self.tabla[1][2],
                              self.tabla[2][0], self.tabla[2][1], self.tabla[2][2])
        return tablero_string

class Casilla:
    def __init__(self, fila, columna):
