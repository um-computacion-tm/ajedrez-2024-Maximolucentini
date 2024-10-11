import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Empty board

    def test_valid_knight_move(self):
        """
        Verifies that the knight can move in an 'L' shape.
        """
        knight = Knight("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, knight)  
        self.assertTrue(knight.is_valid_piece_move(self.__board__, (4, 4), (6, 5)))  # Valid move (2, 1)
        self.assertTrue(knight.is_valid_piece_move(self.__board__, (4, 4), (2, 5)))  # Valid move (2, -1)
        self.assertTrue(knight.is_valid_piece_move(self.__board__, (4, 4), (5, 6)))  # Valid move (1, 2)
        self.assertTrue(knight.is_valid_piece_move(self.__board__, (4, 4), (5, 2)))  # Valid move (1, -2)

    def test_invalid_knight_move(self):
        """
        Verifies that the knight cannot move in an invalid way (not in an 'L' shape).
        """
        knight = Knight("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, knight)
        self.assertFalse(knight.is_valid_piece_move(self.__board__, (4, 4), (4, 6)))  # Horizontal move
        self.assertFalse(knight.is_valid_piece_move(self.__board__, (4, 4), (6, 6)))  # Diagonal move

    def test_knight_capture_enemy_piece(self):
        """
        Verifies that the knight can capture an enemy piece.
        """
        knight = Knight("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, knight)  
        enemy_piece = Knight("BLACK", (6, 5))
        self.__board__.set_piece(6, 5, enemy_piece)
        self.assertTrue(knight.is_valid_piece_move(self.__board__, (4, 4), (6, 5)))  # Capture enemy piece

    def test_knight_capture_own_piece(self):
        """
        Verifies that the knight cannot capture its own piece.
        """
        knight = Knight("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, knight)  
        own_piece = Knight("WHITE", (6, 5))
        self.__board__.set_piece(6, 5, own_piece)
        self.assertFalse(knight.is_valid_piece_move(self.__board__, (4, 4), (6, 5)))  # Cannot capture own piece

    def test_knight_move_out_of_board(self):
        """
        Verifies that the knight cannot move outside the board.
        """
        knight = Knight("WHITE", (7, 7))
        self.__board__.set_piece(7, 7, knight)
        self.assertFalse(knight.is_valid_piece_move(self.__board__, (7, 7), (9, 8)))  # Move outside the board

if __name__ == '__main__':
    unittest.main()
