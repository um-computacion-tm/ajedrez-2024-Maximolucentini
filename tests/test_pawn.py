import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        """Configura el tablero antes de cada prueba."""
        self.board = Board()
        self.board.setup_board()

   