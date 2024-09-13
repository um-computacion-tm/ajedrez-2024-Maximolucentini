import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.setup_board()

