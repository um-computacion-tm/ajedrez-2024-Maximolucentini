import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.chess import Chess
from game.board import Board
from game.pawn import Pawn
from game.king import King

class TestChess(unittest.TestCase):
    def setUp(self):
        """
        Sets up a chess game before each test.
        Initializes a new Chess instance.
        """
        self.__chess_game__ = Chess()

    def test_initialize_pieces(self):
        """
        Verifies that the pieces are correctly positioned at the start of the game.
        Checks the initial placement of pawns and kings.
        """
        board = self.__chess_game__.__board__

        """Verify white pawns"""
        for col in range(8):
            self.assertIsInstance(board.get_piece(6, col), Pawn)
            self.assertEqual(board.get_piece(6, col).get_color(), "WHITE")

        """Verify black pawns"""
        for col in range(8):
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertEqual(board.get_piece(1, col).get_color(), "BLACK")

        """Verify kings"""
        self.assertIsInstance(board.get_piece(7, 4), King)
        self.assertEqual(board.get_piece(7, 4).get_color(), "WHITE")
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertEqual(board.get_piece(0, 4).get_color(), "BLACK")

    def test_switch_turn(self):
        """
        Tests that the turns alternate correctly between players.
        """
        self.assertEqual(self.__chess_game__.__current_turn__, "WHITE")
        self.__chess_game__.__switch_turn__()
        self.assertEqual(self.__chess_game__.__current_turn__, "BLACK")
        self.__chess_game__.__switch_turn__()
        self.assertEqual(self.__chess_game__.__current_turn__, "WHITE")

    def test_is_valid_turn(self):
        """
        Verifies that the correct player is moving their piece.
        """
        board = self.__chess_game__.__board__
        white_pawn = board.get_piece(6, 0)
        black_pawn = board.get_piece(1, 0)

        self.assertTrue(self.__chess_game__.__is_valid_turn__(white_pawn))  # White's turn
        self.__chess_game__.__switch_turn__()
        self.assertTrue(self.__chess_game__.__is_valid_turn__(black_pawn))  # Black's turn

    def test_make_move_valid(self):
        """
        Tests that a valid move is executed correctly.
        Moves a white pawn forward and verifies the board state.
        """
        result, message = self.__chess_game__.make_move((6, 0), (5, 0))  
        """Move white pawn forward"""
        self.assertTrue(result)
        self.assertEqual(message, "WHITE ♙ moved from (6, 0) to (5, 0)")
        self.assertIsInstance(self.__chess_game__.__board__.get_piece(5, 0), Pawn)
        self.assertIsNone(self.__chess_game__.__board__.get_piece(6, 0))

    def test_make_move_invalid(self):
        """
        Tests that an invalid move is not executed.
        Tries to make an invalid move after a valid one and checks the response.
        """
        """Move white pawn from a2 to a4 (valid move)"""
        result, message = self.__chess_game__.make_move((6, 0), (4, 0))
        self.assertTrue(result)

        """Switch turn and attempt invalid move"""
        self.__chess_game__.__switch_turn__()

        """Try to move the same white pawn from a4 to a6 (invalid move)"""
        result, message = self.__chess_game__.make_move((4, 0), (2, 0))  
        """Invalid move"""
        self.assertFalse(result)
        self.assertEqual(message, "Invalid move.")

    def test_end_game_by_agreement(self):
        """
        Tests that the game can end by mutual agreement between players.
        """
        self.__chess_game__.end_game_by_agreement()
        self.assertTrue(self.__chess_game__.__is_game_over__)

    def test_check_end_conditions(self):
        """
        Tests the game end conditions (when a player has no pieces left).
        Simulates the elimination of all pieces of one color and checks the end message.
        """
        """Remove all black pieces"""
        for i in range(8):
            self.__chess_game__.__board__.set_piece(1, i, None) # Remove black pawns
        """Remove the rest of the black pieces"""
        self.__chess_game__.__board__.set_piece(0, 0, None)  # Black rook
        self.__chess_game__.__board__.set_piece(0, 1, None)  # Black knight
        self.__chess_game__.__board__.set_piece(0, 2, None)  # Black bishop
        self.__chess_game__.__board__.set_piece(0, 3, None)  # Black queen
        self.__chess_game__.__board__.set_piece(0, 4, None)  # Black king
        self.__chess_game__.__board__.set_piece(0, 5, None)  # Black bishop
        self.__chess_game__.__board__.set_piece(0, 6, None)  # Black knight
        self.__chess_game__.__board__.set_piece(0, 7, None)  # Black rook

        # Verify no black pieces are left
        black_pieces = self.__chess_game__.__board__.get_pieces("BLACK")
        self.assertEqual(len(black_pieces), 0)  # Confirm all black pieces were removed

        game_over, message = self.__chess_game__.check_end_conditions()
        self.assertTrue(game_over)
        self.assertEqual(message, "Black pieces have been eliminated. White wins!")

        # Remove all white pieces
        self.setUp()  # Reset the game
        for i in range(8):
            self.__chess_game__.__board__.set_piece(6, i, None)  # Remove white pawns
        self.__chess_game__.__board__.set_piece(7, 0, None)  # White rook
        self.__chess_game__.__board__.set_piece(7, 1, None)  # White knight
        self.__chess_game__.__board__.set_piece(7, 2, None)  # White bishop
        self.__chess_game__.__board__.set_piece(7, 3, None)  # White queen
        self.__chess_game__.__board__.set_piece(7, 4, None)  # White king
        self.__chess_game__.__board__.set_piece(7, 5, None)  # White bishop
        self.__chess_game__.__board__.set_piece(7, 6, None)  # White knight
        self.__chess_game__.__board__.set_piece(7, 7, None)  # White rook

        # Verify no white pieces are left
        white_pieces = self.__chess_game__.__board__.get_pieces("WHITE")
        self.assertEqual(len(white_pieces), 0)  # Confirm all white pieces were removed

        game_over, message = self.__chess_game__.check_end_conditions()
        self.assertTrue(game_over)
        self.assertEqual(message, "White pieces have been eliminated. Black wins!")

if __name__ == '__main__':
    unittest.main()
