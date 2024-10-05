from game.piece import Piece
from game.straightmovingpiece import StraightMovingPiece
from game.diagonalmovingpiece import DiagonalMovingPiece

class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__(color, position)
        self.straight_moving_piece = StraightMovingPiece(color)
        self.diagonal_moving_piece = DiagonalMovingPiece(color)

    def symbol(self):
        return '♕' if self.get_color() == "WHITE" else '♛'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para la reina."""
        """La reina puede moverse verticalmente, horizontalmente o en diagonal."""
        """Aprovechar las clases StraightMovingPiece y DiagonalMovingPiece"""
        return self.straight_moving_piece.is_valid_piece_move(board, from_pos, to_pos) or \
               self.diagonal_moving_piece.is_valid_piece_move(board, from_pos, to_pos)

 
    
