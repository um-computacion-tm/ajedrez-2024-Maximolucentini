from game.piece import Piece

class Knight(Piece):
    def __init__(self, color, position=None):
        """
        Initializes a Knight piece with the specified color and position.
        """
        super().__init__(color, position)
        
    def symbol(self):
        """
        Returns the symbol representing the knight.
        Returns:
        str: '♘' for white knights, '♞' for black knights.
        """
        return '♘' if self.get_color() == "WHITE" else '♞'
        
    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the knight.
        The knight moves in an 'L' shape.
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
        
        """Validate the knight's 'L' shape move"""
        return self.__is_knight_move__(from_pos, to_pos)
    
    def __is_knight_move__(self, from_pos, to_pos):
        """
        Checks if the move follows the 'L' shape (valid knight move).
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is a valid knight move, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

