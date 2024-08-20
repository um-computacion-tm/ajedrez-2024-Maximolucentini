from game.piece import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.__initial_position__ = position