from game.piece import Piece
from game.straightmovingpiece import StraightMovingPiece
from game.diagonalmovingpiece import DiagonalMovingPiece

class Queen(Piece):
    def __init__(self, color, position=None):
        """
        Initializes a Queen piece with the specified color and position.
        Uses StraightMovingPiece for vertical/horizontal moves and DiagonalMovingPiece for diagonal moves.
        """
        super().__init__(color, position)
        self.__straight_moving_piece__ = StraightMovingPiece(color)
        self.__diagonal_moving_piece__ = DiagonalMovingPiece(color)

    def symbol(self):
        """
        Returns the symbol representing the queen.
        Returns:
        str: '♕' for white queens, '♛' for black queens.
        """
        return '♕' if self.get_color() == "WHITE" else '♛'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the queen.
        The queen can move vertically, horizontally, or diagonally.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        return self.__straight_moving_piece__.is_valid_piece_move(board, from_pos, to_pos) or \
               self.__diagonal_moving_piece__.is_valid_piece_move(board, from_pos, to_pos)


 
    
