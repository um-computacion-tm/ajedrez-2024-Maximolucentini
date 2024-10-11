import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board

    def test_valid_vertical_move(self):
        """
        Verifies that the rook can move vertically.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        self.assertTrue(rook.is_valid_piece_move(self.__board__, (0, 0), (5, 0)))  # Vertical move

    def test_valid_horizontal_move(self):
        """
        Verifies that the rook can move horizontally.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        self.assertTrue(rook.is_valid_piece_move(self.__board__, (0, 0), (0, 7)))  # Horizontal move

    def test_invalid_diagonal_move(self):
        """
        Verifies that the rook cannot move diagonally.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        self.assertFalse(rook.is_valid_piece_move(self.__board__, (0, 0), (3, 3)))  # Diagonal move

    def test_blocked_move(self):
        """
        Verifies that the rook cannot move through other pieces.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        blocking_piece = Rook("WHITE", (3, 0))
        self.__board__.set_piece(3, 0, blocking_piece)
        self.assertFalse(rook.is_valid_piece_move(self.__board__, (0, 0), (5, 0)))  # Blocked path

    def test_capture_enemy_piece(self):
        """
        Verifies that the rook can capture an enemy piece.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        enemy_piece = Rook("BLACK", (5, 0))
        self.__board__.set_piece(5, 0, enemy_piece)
        self.assertTrue(rook.is_valid_piece_move(self.__board__, (0, 0), (5, 0)))  # Capture enemy piece

    def test_capture_own_piece(self):
        """
        Verifies that the rook cannot capture its own piece.
        """
        rook = Rook("WHITE", (0, 0))
        self.__board__.set_piece(0, 0, rook)
        own_piece = Rook("WHITE", (5, 0))
        self.__board__.set_piece(5, 0, own_piece)
        self.assertFalse(rook.is_valid_piece_move(self.__board__, (0, 0), (5, 0)))  # Cannot capture own piece

if __name__ == '__main__':
    unittest.main()
