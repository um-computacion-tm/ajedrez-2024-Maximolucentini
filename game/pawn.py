from game.piece import Piece
from game.board import *

class Pawn(Piece):
    def __init__(self, color, position=None):
        """
        Initializes a Pawn piece with the specified color and position.
        Attributes:
        __initial_position__: Boolean indicating if the pawn is in its initial position.
        """
        super().__init__(color, position)
        self.__initial_position__ = True  
        """The pawn starts in its initial position"""

    def symbol(self):
        """
        Returns the symbol representing the pawn.
        Returns:
        str: '♙' for white pawns, '♟' for black pawns.
        """
        return '♙' if self.get_color() == "WHITE" else '♟'

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for the pawn.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        direction = -1 if self.get_color() == 'WHITE' else 1

        """Check forward move without capture"""
        if self.__valid_move_forward__(board, from_pos, to_pos, direction):
            return True

        """Check diagonal capture"""
        if self.__valid_diagonal_capture__(board, from_pos, to_pos, direction):
            return True

        return False

    def __valid_move_forward__(self, board, from_pos, to_pos, direction):
        """
        Checks if the forward move is valid (without capture).
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        direction (int): The direction of movement (-1 for white, 1 for black).
        Returns:
        bool: True if the forward move is valid, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        """Move in the same column"""
        if from_col == to_col:
            """Check single step forward"""
            if self.__is_one_step_forward__(board, from_pos, to_pos, direction):
                return True
            """Check double step from initial position"""
            if self.__is_two_steps_forward__(board, from_pos, to_pos, direction):
                return True
        return False

    def __is_one_step_forward__(self, board, from_pos, to_pos, direction):
        """
        Checks if the move is a single step forward and the square is empty.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        direction (int): The direction of movement (-1 for white, 1 for black).
        Returns:
        bool: True if the single step forward is valid, False otherwise.
        """
        from_row, _ = from_pos
        to_row, _ = to_pos
        return from_row + direction == to_row and board.get_piece(to_pos[0], to_pos[1]) is None

    def __is_two_steps_forward__(self, board, from_pos, to_pos, direction):
        """
        Checks if the pawn can move two steps forward from the initial position.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        direction (int): The direction of movement (-1 for white, 1 for black).
        Returns:
        bool: True if the two-step forward move is valid, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, _ = to_pos
        return self.__initial_position__ and from_row + 2 * direction == to_row and \
               board.get_piece(from_row + direction, from_col) is None and \
               board.get_piece(to_pos[0], to_pos[1]) is None

    def __valid_diagonal_capture__(self, board, from_pos, to_pos, direction):
        """
        Checks if the diagonal capture is valid.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        direction (int): The direction of movement (-1 for white, 1 for black).
        Returns:
        bool: True if the diagonal capture is valid, False otherwise.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if abs(from_col - to_col) == 1 and from_row + direction == to_row:
            target_piece = board.get_piece(to_row, to_col)
            return self.__is_enemy_piece__(target_piece)
        return False

    def __is_enemy_piece__(self, target_piece):
        """
        Checks if the target piece is an enemy piece.
        Parameters:
        target_piece (Piece or None): The piece at the destination, or None if the square is empty.
        Returns:
        bool: True if the target piece is an enemy, False if it is an ally or the square is empty.
        """
        return target_piece is not None and target_piece.get_color() != self.get_color()
