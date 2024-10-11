import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.king import King
from game.piece import Piece

class TestKing(unittest.TestCase):

    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board

    def test_valid_move(self):
        """
        Verifies that the king can move one square in any direction.
        """
        king = King("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, king)
        self.assertTrue(king.is_valid_piece_move(self.__board__, (4, 4), (5, 5)))  # Diagonal move
        self.assertTrue(king.is_valid_piece_move(self.__board__, (4, 4), (4, 5)))  # Horizontal move
        self.assertTrue(king.is_valid_piece_move(self.__board__, (4, 4), (5, 4)))  # Vertical move

    def test_invalid_move(self):
        """
        Verifies that the king cannot move more than one square in any direction.
        """
        king = King("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, king)
        self.assertFalse(king.is_valid_piece_move(self.__board__, (4, 4), (6, 4)))  # Invalid move (2 squares vertical)
        self.assertFalse(king.is_valid_piece_move(self.__board__, (4, 4), (4, 6)))  # Invalid move (2 squares horizontal)
        self.assertFalse(king.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  # Invalid move (2 squares diagonal)

    def test_capture_enemy_piece(self):
        """
        Verifies that the king can capture an enemy piece.
        """
        king = King("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, king)
        enemy_piece = King("BLACK", (5, 5))
        self.__board__.set_piece(5, 5, enemy_piece)
        self.assertTrue(king.is_valid_piece_move(self.__board__, (4, 4), (5, 5)))  # Capture enemy piece

    def test_capture_own_piece(self):
        """
        Verifies that the king cannot capture its own piece.
        """
        king = King("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, king)
        own_piece = King("WHITE", (5, 5))
        self.__board__.set_piece(5, 5, own_piece)
        self.assertFalse(king.is_valid_piece_move(self.__board__, (4, 4), (5, 5)))  # Cannot capture own piece

    def test_symbol(self):
        """
        Verifies that the king's symbol is correct for both colors.
        """
        white_king = King("WHITE", (0, 4))
        black_king = King("BLACK", (7, 4))
        self.assertEqual(white_king.symbol(), '♔')  # White king
        self.assertEqual(black_king.symbol(), '♚')  # Black king

if __name__ == '__main__':
    unittest.main()
