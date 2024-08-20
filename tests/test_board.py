import sys
import os

# Agregar la ruta al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import *
from game.rook import *
from game.knight import *
from game.bishop import *
from game.queen import *
from game.king import *
from game.pawn import *

class TestBoardSetup(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_initial_piece_positions(self):
        # Verificar las posiciones iniciales de las piezas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)

        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

        # Verificar las posiciones iniciales de los peones
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)

if __name__ == '__main__':
    unittest.main()
