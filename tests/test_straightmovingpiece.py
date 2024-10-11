import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.straightmovingpiece import StraightMovingPiece
from game.piece import Piece

class TestStraightMovingPiece(unittest.TestCase):

    def setUp(self):
        """
        Sets up a normal board with the initial chess configuration before each test.
        """
        self.__board__ = Board()

    def test_valid_horizontal_move(self):
        """
        Verifies a valid horizontal move on an empty board.
        """
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 5)))  # Horizontal move to the right
    
    def test_valid_vertical_move(self):
        """
        Verifies a valid vertical move on an empty board.
        """
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (5, 2)))  # Vertical move down
    
    def test_invalid_non_straight_move(self):
        """
        Verifies that a non-straight move is invalid on an empty board.
        """
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (3, 3)))  # Diagonal move
    
    def test_blocked_horizontal_move(self):
        """
        Verifies that a blocked horizontal move is invalid.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        blocking_piece = StraightMovingPiece("BLACK", (2, 4))
        self.__board__.set_piece(2, 4, blocking_piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 5)))  # Path blocked by piece at (2, 4)
    
    def test_blocked_vertical_move(self):
        """
        Verifies that a blocked vertical move is invalid.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        blocking_piece = StraightMovingPiece("BLACK", (4, 2))
        self.__board__.set_piece(4, 2, blocking_piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (5, 2)))  # Path blocked by piece at (4, 2)
    
    def test_capture_enemy_piece(self):
        """
        Verifies that a straight-moving piece can capture an enemy piece.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        enemy_piece = StraightMovingPiece("BLACK", (2, 5))
        self.__board__.set_piece(2, 5, enemy_piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 5)))  # Capturing enemy piece
    
    def test_capture_own_piece(self):
        """
        Verifies that a straight-moving piece cannot capture a piece of the same color.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        own_piece = StraightMovingPiece("WHITE", (2, 5))
        self.__board__.set_piece(2, 5, own_piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 5)))  # Cannot capture own piece
    
    def test_move_out_of_board(self):
        """
        Verifies that a move outside the board is invalid.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (8, 2)))  # Out of vertical bounds
    
    def test_move_to_same_position(self):
        """
        Verifies that a piece cannot move to the same position it started from.
        """
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 2)))  # Same position

if __name__ == '__main__':
    unittest.main()
