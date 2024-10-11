from game.piece import Piece

class King(Piece):
    def __init__(self, color, position=None):
        """
        Initializes a King piece with the specified color and position.
        """
        super().__init__(color, position)
        
    def symbol(self):
        """
        Returns the symbol representing the king.
        Returns:
        str: '♔' for white kings, '♚' for black kings.
        """
        return '♔' if self.get_color() == "WHITE" else '♚'
    
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the king.
        The king can move one square in any direction.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        """Ensure the destination is valid (cannot capture own pieces)"""
        if not self.is_valid_destination(board, to_pos):
            return False
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        """The king moves only one square in any direction"""
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1

   