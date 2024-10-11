from game.piece import Piece

class StraightMovingPiece(Piece):

    def is_valid_straight_move(self, from_pos, to_pos):
        """
        Checks if the movement is in a straight line (horizontal or vertical).
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is in a straight line, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return from_row == to_row or from_col == to_col

    def is_path_clear(self, board, from_pos, to_pos):
        """
        Checks if the path is clear for a straight-line move.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the path is clear, False otherwise.
        """
        if not self.is_valid_straight_move(from_pos, to_pos):
            return False

        is_horizontal = from_pos[0] == to_pos[0]
        return self.__verify_path_clear__(board, from_pos, to_pos, is_horizontal)

    def __verify_path_clear__(self, board, from_pos, to_pos, is_horizontal):
        """
        Verifies if the path (horizontal or vertical) is clear between two positions.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        is_horizontal (bool): Whether the move is horizontal or not.
        Returns:
        bool: True if the path is clear, False otherwise.
        """
        start_pos, end_pos, fixed_pos = self.__get_positions__(from_pos, to_pos, is_horizontal)

        check_position = (lambda pos: board.get_piece(fixed_pos, pos)) if is_horizontal else \
                         (lambda pos: board.get_piece(pos, fixed_pos))

        for pos in range(min(start_pos, end_pos) + 1, max(start_pos, end_pos)):
            if check_position(pos) is not None:
                return False
        return True

    def __get_positions__(self, from_pos, to_pos, is_horizontal):
        """
        Retrieves the start, end, and fixed positions based on the type of movement.
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        is_horizontal (bool): Whether the move is horizontal or not.
        Returns:
        tuple: The start position, end position, and fixed position.
        """
        if is_horizontal:
            return from_pos[1], to_pos[1], from_pos[0]
        else:
            return from_pos[0], to_pos[0], from_pos[1]

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for straight-moving pieces.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        return (self.__is_within_board__(to_pos) 
                and not self.__is_same_position__(from_pos, to_pos)
                and self.is_valid_straight_move(from_pos, to_pos)
                and self.is_path_clear(board, from_pos, to_pos)
                and self.is_valid_destination(board, to_pos))

    def __is_within_board__(self, pos):
        """
        Validates if a position is within the board boundaries.
        Parameters:
        pos (tuple): The position to check as (row, col).
        Returns:
        bool: True if the position is within bounds, False otherwise.
        """
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    def __is_same_position__(self, from_pos, to_pos):
        """
        Validates if the starting and destination positions are the same.
        Parameters:
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the positions are the same, False otherwise.
        """
        return from_pos == to_pos








