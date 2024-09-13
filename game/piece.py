
class Piece:
    def __init__(self, color, position=None):
        self.color= color  
        """Color de la pieza, "WHITE" o "BLACK". """
        self.__position__ = position  
        """Posición inicial de la pieza, como una tupla (fila, columna)"""
        
    def symbol(self):
        """Devuelve un símbolo que representa la pieza. Este método se sobrescribirá en las subclases."""
        raise NotImplementedError    
        
    def get_color(self):
        """Devuelve el color de la pieza."""
        return self.color
    
    def get_position(self):
        """Devuelve la posición actual de la pieza."""
        return self.__position__

    def set_position(self, position):
        """Establece la nueva posición de la pieza."""
        self.__position__ = position

    def is_valid_destination(self, board, to_row, to_col):
        """Verificar si la posición de destino está dentro del tablero y no está ocupada por una pieza del mismo color"""
        if to_row < 0 or to_row >= 8 or to_col < 0 or to_col >= 8:
            return False
        piece = board.get_piece(to_row, to_col)
        if piece and piece.get_color() == self.get_color():
            return False
        return True

   
 
    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verificar si el movimiento es válido para la pieza."""
        raise NotImplementedError("Esta función debe ser implementada por las subclases.")



    def move(self, to_row, to_col):
        """Actualiza la posición de la pieza."""
        self.set_position((to_row, to_col))

    def __str__(self):
        return f"{self.color} Piece at {self.__position__}"