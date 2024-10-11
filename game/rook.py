from game.straightmovingpiece import StraightMovingPiece

class Rook(StraightMovingPiece):
    def __init__(self, color, position=None):
        """
        Initializes a Rook piece with the specified color and position.
        """
        super().__init__(color, position)
        
    def symbol(self):
        """
        Returns the symbol representing the rook.
        Returns:
        str: '♖' for white rooks, '♜' for black rooks.
        """
        return '♖' if self.get_color() == "WHITE" else '♜'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the rook.
        The rook can move vertically or horizontally.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        """The rook moves vertically or horizontally, calling the base class validation"""
        return super().is_valid_piece_move(board, from_pos, to_pos)
