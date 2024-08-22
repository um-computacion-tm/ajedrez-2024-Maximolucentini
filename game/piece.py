class Piece:
    def __init__(self, color, position=None):
        self.__color__ = color
        self.__position__ = position
      
    @property
    def color(self):
        return self.__color__

    @property
    def position(self):
        return self.__position__

    @position.setter
    def position(self, new_position):
        self.__position__ = new_position

    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # Esta función deberá ser implementada en cada subclase.
        raise NotImplementedError