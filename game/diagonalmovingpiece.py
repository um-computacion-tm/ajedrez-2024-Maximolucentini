from game.piece import Piece

class DiagonalMovingPiece(Piece):
    def is_valid_diagonal_move(self, from_pos, to_pos):
        """
        Checks if the move is diagonal.
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is diagonal, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return abs(from_row - to_row) == abs(from_col - to_col)

    def get_diagonal_steps(self, from_pos, to_pos):
        """
        Gets the steps for the diagonal move.
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        tuple: A tuple containing the row and column steps for the diagonal move.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        return row_step, col_step

    def check_clear_path(self, board, from_pos, to_pos, steps):
        """
        Checks if the diagonal path is clear.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        steps (tuple): The row and column steps for the diagonal move.
        Returns:
        bool: True if the path is clear, False otherwise.
        """
        row_step, col_step = steps
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        current_row, current_col = from_row + row_step, from_col + col_step

        """Traverse the intermediate path until the final position"""
        while (current_row, current_col) != (to_row, to_col):
            if board.get_piece(current_row, current_col) is not None:
                return False  
            """Path blocked"""

            current_row += row_step
            current_col += col_step

        """Use the base class's is_valid_destination to validate the destination"""
        return self.is_valid_destination(board, to_pos)

    def is_path_clear(self, board, from_pos, to_pos):
        """
        Checks if the path is clear for the diagonal move.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the path is clear, False otherwise.
        """
        if not self.is_valid_diagonal_move(from_pos, to_pos):
            return False
        
        row_step, col_step = self.get_diagonal_steps(from_pos, to_pos)
        return self.check_clear_path(board, from_pos, to_pos, (row_step, col_step))

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for diagonal-moving pieces.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        if not self.is_valid_diagonal_move(from_pos, to_pos):
            return False

        if not self.is_path_clear(board, from_pos, to_pos):
            return False

        return True
