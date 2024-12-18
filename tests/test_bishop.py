import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.bishop import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Empty board"""

    def test_valid_diagonal_move(self):
        """
        Verifies that the bishop can move diagonally.
        """
        bishop = Bishop("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, bishop)
        self.assertTrue(bishop.is_valid_piece_move(self.__board__, (4, 4), (7, 7)))  
        """Diagonal move"""

    def test_blocked_move(self):
        """
        Verifies that the bishop cannot move through other pieces.
        """
        bishop = Bishop("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, bishop)
        blocking_piece = Bishop("WHITE", (6, 6))
        self.__board__.set_piece(6, 6, blocking_piece)
        self.assertFalse(bishop.is_valid_piece_move(self.__board__, (4, 4), (7, 7)))  
        """Path blocked"""

    def test_capture_enemy_piece(self):
        """
        Verifies that the bishop can capture an enemy piece.
        """
        bishop = Bishop("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, bishop)
        enemy_piece = Bishop("BLACK", (6, 6))
        self.__board__.set_piece(6, 6, enemy_piece)
        self.assertTrue(bishop.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  
        """Capture enemy piece"""

    def test_capture_own_piece(self):
        """
        Verifies that the bishop cannot capture its own piece.
        """
        bishop = Bishop("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, bishop)
        own_piece = Bishop("WHITE", (6, 6))
        self.__board__.set_piece(6, 6, own_piece)
        self.assertFalse(bishop.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  
        """Cannot capture own piece"""

    def test_invalid_move(self):
        """
        Verifies that the bishop cannot move in non-diagonal directions.
        """
        bishop = Bishop("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, bishop)
        self.assertFalse(bishop.is_valid_piece_move(self.__board__, (4, 4), (4, 7)))  
        """Non-diagonal move"""

    def test_symbol(self):
        """
        Verifies that the bishop's symbol is correct for both colors.
        """
        white_bishop = Bishop("WHITE", (0, 2))
        black_bishop = Bishop("BLACK", (7, 2))
        self.assertEqual(white_bishop.symbol(), '♗')  
        """White bishop"""
        self.assertEqual(black_bishop.symbol(), '♝')  
        """Black bishop"""

if __name__ == '__main__':
    unittest.main()


    





