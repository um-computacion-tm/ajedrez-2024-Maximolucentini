from game.movement import Movement
class Piece:
    def __init__(self, color, position=None):
        self.__color__ = color  # Color de la pieza, "WHITE" o "BLACK"
        self.__position__ = position  # Posición inicial de la pieza, como una tupla (fila, columna)
        self.movement_validator = Movement()  # Agrega un atributo movement_validator
    
    def get_color(self):
        """Devuelve el color de la pieza."""
        return self.__color__
    
    def get_position(self):
        """Devuelve la posición actual de la pieza."""
        return self.__position__

    def set_position(self, position):
        """Establece la nueva posición de la pieza."""
        self.__position__ = position

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # Verifica si la posición de destino está dentro del tablero
        if to_row < 0 or to_row >= 8 or to_col < 0 or to_col >= 8:
            return False

        # Verifica si la posición de destino está ocupada por una pieza del mismo tipo
        if board[to_row][to_col] and board[to_row][to_col].get_color() == self.__color__:
            return False

        # Utiliza la lógica de los movimientos para verificar si el movimiento es válido
        return self.movement_validator.is_valid_move(board, from_row, from_col, to_row, to_col)

    def move(self, to_row, to_col):
        """Actualiza la posición de la pieza."""
        self.set_position((to_row, to_col))

    def __str__(self):
        return f"{self.__color__} Piece at {self.__position__}"