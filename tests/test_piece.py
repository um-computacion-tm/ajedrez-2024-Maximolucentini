import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.piece import Piece
from game.board import Board  

class TestPiece(unittest.TestCase):

    def setUp(self):
        """
        Sets up a piece and a real board before each test.
        Creates a white piece at position (0, 0) and initializes the board.
        """
        self.__piece__ = Piece("WHITE", (0, 0))  # Create a white piece at position (0, 0)
        self.__board__ = Board()  # Use the board
        self.__board__.__setup_board__  # Initialize the board with pieces

    def test_get_color(self):
        """
        Tests that get_color returns the correct color of the piece.
        """
        self.assertEqual(self.__piece__.get_color(), "WHITE")

    def test_get_position(self):
        """
        Tests that get_position returns the correct position of the piece.
        """
        self.assertEqual(self.__piece__.get_position(), (0, 0))

    def test_set_position(self):
        """
        Tests that set_position correctly sets the new position of the piece.
        """
        self.__piece__.set_position((1, 1))
        self.assertEqual(self.__piece__.get_position(), (1, 1))

    def test_is_valid_destination_within_bounds(self):
        """
        Tests that is_valid_destination returns True when the destination is within the board
        and not occupied by a piece of the same color.
        """
        self.assertTrue(self.__piece__.is_valid_destination(self.__board__, (4, 4)))  # Test with a tuple

    def test_is_valid_destination_out_of_bounds(self):
        """
        Tests that is_valid_destination returns False when the destination is out of bounds.
        """
        self.assertFalse(self.__piece__.is_valid_destination(self.__board__, (8, 8)))  # Test with a tuple

    def test_is_valid_destination_occupied_by_same_color(self):
        """
        Tests that is_valid_destination returns False when the destination is occupied by a piece of the same color.
        """
        piece_on_board = Piece("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, piece_on_board)
        self.assertFalse(self.__piece__.is_valid_destination(self.__board__, (4, 4)))  # Test with a tuple

    def test_is_valid_destination_occupied_by_opponent(self):
        """
        Tests that is_valid_destination returns True when the destination is occupied by an opponent's piece.
        """
        opponent_piece = Piece("BLACK", (4, 4))
        self.__board__.set_piece(4, 4, opponent_piece)
        self.assertTrue(self.__piece__.is_valid_destination(self.__board__, (4, 4)))  # Test with a tuple

    def test_move(self):
        """
        Tests that move correctly updates the position of the piece.
        """
        self.__piece__.move(3, 3)
        self.assertEqual(self.__piece__.get_position(), (3, 3))

    def test_str(self):
        """
        Tests the string representation of the Piece object.
        """
        self.assertEqual(str(self.__piece__), "WHITE Piece at (0, 0)")

if __name__ == '__main__':
    unittest.main()
