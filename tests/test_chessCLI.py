import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from game.chessCLI import ChessCLI

class TestChessCLI(unittest.TestCase):
    
    @patch('builtins.print')
    def test_display_board(self, mock_print):
        """
        Test that the chess board is displayed correctly.

        What it receives:
        - mock_print: A mock for capturing output from print.

        What it does:
        - Calls the display_board method to print the chess board to the console.
        - Verifies that the column headers and row numbers are printed.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.display_board()
        mock_print.assert_any_call("  a b c d e f g h")
        mock_print.assert_any_call(8, end=" ")
        mock_print.assert_any_call(1, end=" ")

    @patch('builtins.input', side_effect=['e2', 'e4'])
    @patch('builtins.print')
    def test_get_move_input(self, mock_print, mock_input):
        """
        Test that the player's move input is correctly processed.

        What it receives:
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock that simulates valid inputs for the move.

        What it does:
        - Simulates user input for moves and verifies that the input is correctly 
          converted into board coordinates.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        from_pos, to_pos = cli.get_move_input()

        self.assertEqual(from_pos, (6, 4))  
        """'e2' -> (6, 4)"""
        self.assertEqual(to_pos, (4, 4))    
        """'e4' -> (4, 4)"""

    @patch('builtins.input', side_effect=['n', 'e2', 'e4', 'n', 'e7', 'e5', 'n', 'g1', 'f3', 'y'])
    @patch('builtins.print')
    @patch('game.chess.Chess.make_move', return_value=(True, "Valid move"))
    @patch('game.chess.Chess.check_end_conditions', return_value=(False, None))
    def test_play_game(self, mock_check_end_conditions, mock_make_move, mock_print, mock_input):
        """
        Test the general game flow with alternating turns.

        What it receives:
        - mock_check_end_conditions: A mock for simulating the game's end conditions.
        - mock_make_move: A mock for simulating valid moves.
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock simulating player inputs for moves and game-ending decisions.

        What it does:
        - Simulates a game with multiple moves and turn-based inputs, verifying moves and
          checking game end conditions after each move.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.play_game()

        mock_print.assert_any_call("Welcome to the chess game.")
        mock_input.assert_any_call("Do you want to end the game? (y/n): ")

        mock_make_move.assert_any_call((6, 4), (4, 4))  
        """White pawn from 'e2' to 'e4'"""
        mock_make_move.assert_any_call((1, 4), (3, 4))  
        """Black pawn from 'e7' to 'e5'"""
        mock_make_move.assert_any_call((7, 6), (5, 5))  
        """White knight from 'g1' to 'f3'"""

        mock_print.assert_any_call("Valid move")
        self.assertEqual(mock_check_end_conditions.call_count, 3)

    @patch('builtins.input', side_effect=['y'])
    @patch('builtins.print')
    @patch('game.chess.Chess.end_game_by_agreement')
    @patch('game.chess.Chess.check_end_conditions', return_value=(True, "Game ended by mutual agreement"))
    def test_end_game_by_agreement(self, mock_check_end_conditions, mock_end_game_by_agreement, mock_print, mock_input):
        """
        Test that the game can end by mutual agreement.

        What it receives:
        - mock_check_end_conditions: A mock for simulating the end game check.
        - mock_end_game_by_agreement: A mock for simulating ending the game by agreement.
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock simulating the player agreeing to end the game.

        What it does:
        - Simulates the player choosing to end the game by mutual agreement.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.play_game()

        mock_end_game_by_agreement.assert_called_once()
        mock_print.assert_any_call("The game has ended by mutual agreement.")
        
    @patch('builtins.input', side_effect=['y'])
    @patch('builtins.print')
    @patch('game.chess.Chess.end_game_by_agreement')
    def test_terminate_game(self, mock_end_game_by_agreement, mock_print, mock_input):
        """
        Test that the game terminates when players choose to end it.

        What it receives:
        - mock_end_game_by_agreement: A mock for simulating ending the game by agreement.
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock simulating the players agreeing to terminate the game.

        What it does:
        - Simulates the game terminating when players choose to end it early.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.play_game()

        mock_end_game_by_agreement.assert_called_once()
        mock_print.assert_any_call("The game has ended by mutual agreement.")
        mock_print.assert_any_call("The game has ended.")  

    
    @patch('builtins.input', side_effect=['n', 'e2', 'e4', 'n', 'e7', 'e5', 'y'])
    @patch('builtins.print')
    @patch('game.chess.Chess.make_move', return_value=(True, "Valid move"))
    @patch('game.chess.Chess.check_end_conditions', return_value=(True, "Game over, one player ran out of pieces"))
    def test_game_end_conditions(self, mock_check_end_conditions, mock_make_move, mock_print, mock_input):
        """
        Test that game end conditions are handled correctly.

        What it receives:
        - mock_check_end_conditions: A mock for simulating the game-ending condition.
        - mock_make_move: A mock for simulating valid moves.
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock simulating player inputs and moves.

        What it does:
        - Simulates moves and verifies that the game end condition is correctly handled.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.play_game()

        mock_print.assert_any_call("Valid move")  
        mock_print.assert_any_call("Game over, one player ran out of pieces")
        mock_print.assert_any_call("The game has ended.")
        
        
    @patch('builtins.input', side_effect=['n', 'e2', 'e4', 'n', 'e7', 'e5', 'n', 'g1', 'f3', 'y'])
    @patch('builtins.print')
    @patch('game.chess.Chess.make_move', side_effect=[(True, "Valid move"), (True, "Valid move"), (True, "Valid move")])
    @patch('game.chess.Chess.check_end_conditions', side_effect=[(False, None), (False, None), (True, "Game over")])
    def test_game_ends_after_move(self, mock_check_end_conditions, mock_make_move, mock_print, mock_input):
        """
        Test that the game ends after a valid move and end conditions are met.

        What it receives:
        - mock_check_end_conditions: A mock that simulates the end of the game.
        - mock_make_move: A mock that simulates a valid move.
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock that simulates player inputs for moves and ending the game.

        What it does:
        - Simulates a valid move followed by the game reaching its end condition.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        cli.play_game()

        mock_make_move.assert_any_call((6, 4), (4, 4))  
        """'e2' -> 'e4'"""
        mock_make_move.assert_any_call((1, 4), (3, 4))  
        """'e7' -> 'e5'"""

        self.assertEqual(mock_check_end_conditions.call_count, 3)
        mock_print.assert_any_call("Game over")
        
    
    
    @patch('builtins.input', side_effect=['n', 'invalid', 'e2', 'e4'])
    @patch('builtins.print')
    def test_get_move_input_invalid(self, mock_print, mock_input):
        """
        Test for handling invalid input in get_move_input.

        What it receives:
        - mock_print: A mock for capturing output from print.
        - mock_input: A mock simulating invalid inputs followed by a valid input.

        What it does:
        - Simulates invalid inputs causing ValueError, followed by valid input.

        What it returns:
        - None.
        """
        cli = ChessCLI()
        from_pos, to_pos = cli.get_move_input()

        self.assertEqual(from_pos, (6, 4))  
        """'e2' -> (6, 4)"""
        self.assertEqual(to_pos, (4, 4))    
        """'e4' -> (4, 4)"""

        self.assertEqual(mock_print.call_count, 1)  
        """one errors + valid move"""
        mock_print.assert_any_call("Invalid input. Please try again.")

if __name__ == '__main__':
    unittest.main()

