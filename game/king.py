from game.piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
