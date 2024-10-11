import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board

    def test_valid_straight_move(self):
        """
        Verifies that the queen can move in a straight line (horizontal, vertical).
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        self.assertTrue(queen.is_valid_piece_move(self.__board__, (4, 4), (4, 7)))  # Horizontal move
        self.assertTrue(queen.is_valid_piece_move(self.__board__, (4, 4), (7, 4)))  # Vertical move

    def test_valid_diagonal_move(self):
        """
        Verifies that the queen can move diagonally.
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        self.assertTrue(queen.is_valid_piece_move(self.__board__, (4, 4), (7, 7)))  # Diagonal move
        self.assertTrue(queen.is_valid_piece_move(self.__board__, (4, 4), (1, 1)))  # Reverse diagonal move

    def test_blocked_move(self):
        """
        Verifies that the queen cannot move through other pieces.
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        blocking_piece = Queen("WHITE", (6, 6))
        self.__board__.set_piece(6, 6, blocking_piece)
        self.assertFalse(queen.is_valid_piece_move(self.__board__, (4, 4), (7, 7)))  # Path blocked

    def test_capture_enemy_piece(self):
        """
        Verifies that the queen can capture an enemy piece.
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        enemy_piece = Queen("BLACK", (6, 6))
        self.__board__.set_piece(6, 6, enemy_piece)
        self.assertTrue(queen.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  # Capture enemy piece

    def test_capture_own_piece(self):
        """
        Verifies that the queen cannot capture its own piece.
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        own_piece = Queen("WHITE", (6, 6))
        self.__board__.set_piece(6, 6, own_piece)
        self.assertFalse(queen.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  # Cannot capture own piece

    def test_invalid_move(self):
        """
        Verifies that the queen cannot move in invalid patterns.
        """
        queen = Queen("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, queen)
        self.assertFalse(queen.is_valid_piece_move(self.__board__, (4, 4), (5, 6)))  # Invalid move (neither straight nor diagonal)

    def test_symbol(self):
        """
        Verifies that the queen's symbol is correct for both colors.
        """
        white_queen = Queen("WHITE", (0, 3))
        black_queen = Queen("BLACK", (7, 3))
        self.assertEqual(white_queen.symbol(), '♕')  # White queen
        self.assertEqual(black_queen.symbol(), '♛')  # Black queen

if __name__ == '__main__':
    unittest.main()

