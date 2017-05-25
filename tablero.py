#combinaciones ganadoras
class Tablero:
    """gestiona las casillas del juego"""
    tabla = []

    # combinaciones_ganadoras = (
    #     [[(x, y) for y in range(3)] for x in range(3)] + # combinaciones horizontales
    #     [[(x, y) for x in range(3)] for y in range(3)] + # combinaciones verticales
    #     [[(d, d) for d in range(3)]] + # diagonal principal
    #     [[(2-d, d) for d in range(3)]] # diagonal secundaria.
    # )

    combinaciones_ganadoras = (
        [(0, 1, 2), (3, 4, 5), (6, 7, 8)] + # combinaciones horizontales
        [(0, 3, 6), (1, 4, 7), (2, 5, 8)] + # combinaciones verticales
        [(0, 4, 8)] + # diagonal principal
        [(2, 4, 6)] # diagonal secundaria.
    )

    def __init__(self):
        """carga el tablero"""
        self.generar_tablero()

    def generar_tablero(self):
        """genera un nuevo tablero"""
        self.tabla = []
        for codigo_casilla in range(1, 10):
            self.tabla.append(Casilla(codigo_casilla))

        return self.tabla

    def buscar_ganador(self, jugada):
        """busca un ganador según su ficha"""
        combinaciones_posibles = self.combinaciones_para_jugada(jugada.casilla)
        print("\n " + str(combinaciones_posibles))
        for combinacion_ganadora in combinaciones_posibles:
            #obtiene las combinaciones ganadores para la casilla seleccionada.
            valores = [str(self.tabla[x]) for x in combinacion_ganadora]
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

    def marcar_casilla(self, jugada):
        """marca una ficha en la casilla indicada"""
        casilla_a_marcar = self.tabla[jugada.casilla]
        print(str(jugada.casilla))
        if not casilla_a_marcar.habilitada:
            return False
        else:
            casilla_a_marcar.valor = jugada.ficha
            casilla_a_marcar.habilitada = False
            self.tabla[jugada.casilla] = casilla_a_marcar
            return True

    def casillas_disponibles(self):
        """obtiene las casillas disponibles"""
        casillas_disponibles = []
        for casilla in self.tabla:
            if casilla.habilitada:
                casillas_disponibles.append(casilla)
        return casillas_disponibles

    def __str__(self):
        tablero_string = ("        |       |       \n"
                          "    {0}   |   {1}   |   {2}   \n"
                          "________|_______|_______\n"
                          "        |       |       \n"
                          "    {3}   |   {4}   |   {5}   \n"
                          "________|_______|_______\n"
                          "        |       |       \n"
                          "    {6}   |   {7}   |   {8}   \n"
                          "        |       |       ").format(str(self.tabla[0]),
                                                             str(self.tabla[1]),
                                                             str(self.tabla[2]),
                                                             str(self.tabla[3]),
                                                             str(self.tabla[4]),
                                                             str(self.tabla[5]),
                                                             str(self.tabla[6]),
                                                             str(self.tabla[7]),
                                                             str(self.tabla[8]))
        return tablero_string

class Casilla:
    """Define la estructura de las casillas"""
    def __init__(self, indice):
        """
            Inicializa una casilla
            la casilla ayuda a manejar el tablero de forma más
            amigable
        """
        self.indice = indice
        self.habilitada = True
        self.valor = ""

    def __str__(self):
        if not self.valor:
            return str(self.indice)
        return self.valor

class Jugada:
    """Para unificar la estructura de una jugada"""
    def __init__(self, casilla, ficha):
        self.casilla = casilla
        self.ficha = ficha

