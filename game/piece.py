class Piece:
    def __init__(self, color, position=None):
        self.__color__ = color  # Color de la pieza, "WHITE" o "BLACK"
        self.__position__ = position  # Posición inicial de la pieza, como una tupla (fila, columna)
    
    def get_color(self):
        #Devuelve el color de la pieza.
        return self.__color__
    
    def get_position(self):
        #Devuelve la posición actual de la pieza.
        return self.__position__

    def set_position(self, position):
        #Establece la nueva posición de la pieza.
        self.__position__ = position

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        #Verifica si un movimiento es válido para la pieza.

        raise NotImplementedError
    
    def move(self, to_row, to_col):

        #Actualiza la posición de la pieza.
       
        self.position = (to_row, to_col)

    def __str__(self):
        return f"{self.__color__} Piece at {self.__position__}"
