from game.diagonalmovingpiece import DiagonalMovingPiece

class Bishop(DiagonalMovingPiece):
    def __init__(self, color, position=None):
        """
        Initializes a Bishop piece with the specified color and position.
        """
        super().__init__(color, position)
        
    def symbol(self):
        """
        Returns the symbol representing the bishop.
        Returns:
        str: '♗' for white bishops, '♝' for black bishops.
        """
        return '♗' if self.get_color() == "WHITE" else '♝'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the bishop.
        The bishop moves diagonally.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        return super().is_valid_piece_move(board, from_pos, to_pos)

    
    