import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.pawn import Pawn
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        """
        Sets up a board before each test.
        Initializes a new Board instance.
        """
        self.__board__ = Board()

    def test_initial_setup(self):
        """
        Verifies that the board is correctly set up at the start of the game.
        Checks pawns and rooks in their initial positions.
        """
        #Verify pawns in their initial positions
        for col in range(8):
            self.assertIsInstance(self.__board__.get_piece(1, col), Pawn)
            self.assertEqual(self.__board__.get_piece(1, col).get_color(), "BLACK")
            self.assertIsInstance(self.__board__.get_piece(6, col), Pawn)
            self.assertEqual(self.__board__.get_piece(6, col).get_color(), "WHITE")

        # Verify rooks in their initial positions
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertEqual(self.__board__.get_piece(0, 0).get_color(), "BLACK")
        self.assertIsInstance(self.__board__.get_piece(7, 0), Rook)
        self.assertEqual(self.__board__.get_piece(7, 0).get_color(), "WHITE")

    def test_get_piece(self):
        """
        Tests the get_piece method at different positions.
        Ensures that empty cells return None.
        """
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook) # An empty cell should return None
        self.assertIsNone(self.__board__.get_piece(3, 3))

    def test_set_piece(self):
        """
        Tests the set_piece method to place a piece at a specific position.
        Verifies that the piece is correctly set on the board.
        """
        rook = Rook("WHITE")
        self.__board__.set_piece(3, 3, rook)
        self.assertIs(self.__board__.get_piece(3, 3), rook)

    def test_is_valid_move(self):
        """
        Tests valid and invalid moves on the board.
        Ensures that initial moves for pawns are handled correctly.
        """
        pawn = self.__board__.get_piece(6, 0)

        """Moving one square should be valid"""
        self.assertTrue(self.__board__.is_valid_move(6, 0, 5, 0))  
        """White pawn from 6,0 to 5,0"""

        """After moving, the initial position flag should be False"""
        self.__board__.move_piece(6, 0, 5, 0)

        """Now moving two squares should be invalid"""
        self.assertFalse(self.__board__.is_valid_move(5, 0, 3, 0))  
        """White pawn cannot move two squares"""

    def test_move_piece(self):
        """
        Tests that a piece is moved correctly on the board.
        Verifies that the original position is emptied and the new position is occupied.
        """
        """Move a white pawn forward"""
        self.__board__.move_piece(6, 0, 5, 0)  
        self.assertIsInstance(self.__board__.get_piece(5, 0), Pawn)
        """The original position should be empty"""
        self.assertIsNone(self.__board__.get_piece(6, 0))
        
    def test_invalid_move(self):
        """
        Tests that invalid moves raise a ValueError.
        Includes moving from an empty square and moving to an occupied square by a friendly piece.
        """
        """Try moving from an empty position"""
        with self.assertRaises(ValueError):
            self.__board__.move_piece(3, 3, 4, 3)

        """Try moving to a square occupied by a piece of the same color"""
        with self.assertRaises(ValueError):
            self.__board__.move_piece(0, 0, 0, 1)  
            """Black rook cannot move to where the black knight is"""

    def test_show_board(self):
        """
        Verifies that the show_board method returns a correct textual representation of the board.
        Ensures that the representation contains 8 rows.
        """
        board_str = self.__board__.show_board()
        self.assertIsInstance(board_str, str)
        """Verify that the representation contains 8 rows"""
        self.assertEqual(len(board_str.strip().split("\n")), 8)

    def test_pawn_initial_position(self):
        """
        Tests that the pawn correctly updates its initial_position status after the first move.
        Ensures that the pawn cannot move two squares after the initial move.
        """
        """Move the pawn for the first time"""
        self.__board__.move_piece(6, 0, 4, 0)

        """Verify that the pawn is no longer in its initial position"""
        pawn = self.__board__.get_piece(4, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertFalse(pawn.__initial_position__)  
        """Should be False after the first move"""

        """Trying to move it two squares again should be invalid"""
        self.assertFalse(self.__board__.is_valid_move(4, 0, 2, 0))  
        """Should not be able to move two squares"""
        
    def test_get_pieces_in_row(self):
        """
        Verifies that pieces of a specific color in a given row are correctly returned.
        """
        white_pieces_row_6 = self.__board__.get_pieces_in_row(6, "WHITE")
        self.assertEqual(len(white_pieces_row_6), 8)  
        """There are 8 white pawns in row 6"""
        self.assertTrue(all(piece.get_color() == "WHITE" for piece in white_pieces_row_6))

        black_pieces_row_1 = self.__board__.get_pieces_in_row(1, "BLACK")
        self.assertEqual(len(black_pieces_row_1), 8)  
        """There are 8 black pawns in row 1"""
        self.assertTrue(all(piece.get_color() == "BLACK" for piece in black_pieces_row_1))

    def test_get_pieces(self):
        """
        Verifies that all pieces of a specific color on the board are correctly returned.
        """
        white_pieces = self.__board__.get_pieces("WHITE")
        self.assertEqual(len(white_pieces), 16)  
        """There are 16 white pieces on the board"""
        self.assertTrue(all(piece.get_color() == "WHITE" for piece in white_pieces))

        black_pieces = self.__board__.get_pieces("BLACK")
        self.assertEqual(len(black_pieces), 16)  
        """There are 16 black pieces on the board"""
        self.assertTrue(all(piece.get_color() == "BLACK" for piece in black_pieces))

if __name__ == '__main__':
    unittest.main()
