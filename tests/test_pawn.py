import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.piece import *
from game.board import *
from game.pawn import *

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        self.__board__ = Board()
        self.__white_pawn__ = Pawn("WHITE", (6, 0))
        self.__black_pawn__ = Pawn("BLACK", (1, 0))
        self.__board__.__positions__[6][0] = self.__white_pawn__
        self.__board__.__positions__[1][0] = self.__black_pawn__

    def test_pawn_initialization(self):
        pawn = Pawn("WHITE", (6, 0))
        self.assertEqual(pawn.get_color(), "WHITE")
        self.assertEqual(pawn.get_position(), (6, 0))
        self.assertEqual(pawn.__initial_position__, (6, 0))

    def test_initial_move_two_squares(self):
        self.assertTrue(self.__white_pawn__.is_valid_move(self.__board__, 6, 0, 4, 0))

    def test_single_step_move(self):
        self.__white_pawn__.move(5, 0)
        self.assertTrue(self.__white_pawn__.is_valid_move(self.__board__, 5, 0, 4, 0))
        self.__white_pawn__.move(4, 0)
        self.assertEqual(self.__white_pawn__.get_position(), (4, 0))

    def test_invalid_two_step_move_after_initial(self):
        self.__white_pawn__.move(5, 0)  # Blanco avanza un paso
        self.assertFalse(self.__white_pawn__.is_valid_move(self.__board__, 5, 0, 3, 0))  # No puede avanzar dos pasos ahora

    def test_valid_capture(self):
        black_pawn = Pawn("BLACK", (5, 1))
        self.__board__.__positions__[5][1] = black_pawn
        self.assertTrue(self.__white_pawn__.is_valid_move(self.__board__, 6, 0, 5, 1))  # Blanco captura diagonalmente
if __name__ == '__main__':
    unittest.main()
