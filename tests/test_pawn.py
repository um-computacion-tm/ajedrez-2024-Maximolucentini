import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        """
        Sets up the board before each test.
        """
        self.__board__ = Board()
        self.__board__.__setup_board__

    def test_pawn_move_one_square_forward(self):
        """
        Tests that a pawn can move one square forward.
        """
        pawn = self.__board__.get_piece(6, 0)
        # Test a valid one-square forward move
        self.assertTrue(pawn.is_valid_piece_move(self.__board__, (6, 0), (5, 0)))

    def test_pawn_move_two_squares_from_initial(self):
        """
        Tests that a pawn can move two squares forward from its initial position.
        """
        pawn = self.__board__.get_piece(6, 0)
        # Test a valid two-square forward move from the initial position
        self.assertTrue(pawn.is_valid_piece_move(self.__board__, (6, 0), (4, 0)))
        
        # After moving, it should not be able to move another two squares
        self.__board__.move_piece(6, 0, 4, 0)
        self.assertFalse(pawn.is_valid_piece_move(self.__board__, (4, 0), (2, 0)))

    def test_pawn_capture_diagonal(self):
        """
        Tests that a pawn can capture an enemy piece diagonally.
        """
        # Move black pawn forward to allow capture
        self.__board__.move_piece(1, 1, 3, 1)
        
        # Move white pawn diagonally to capture the black pawn
        pawn = self.__board__.get_piece(6, 0)
        self.__board__.move_piece(6, 0, 4, 0)
        self.assertTrue(pawn.is_valid_piece_move(self.__board__, (4, 0), (3, 1)))

    def test_pawn_invalid_move(self):
        """
        Tests that an invalid move is not allowed for the pawn.
        """
        pawn = self.__board__.get_piece(1, 0)
        
        # Invalid move: diagonal without capture
        self.assertFalse(pawn.is_valid_piece_move(self.__board__, (1, 0), (2, 1)))
        
        # Invalid move: moving backward
        self.assertFalse(pawn.is_valid_piece_move(self.__board__, (1, 0), (0, 0)))

if __name__ == '__main__':
    unittest.main()
