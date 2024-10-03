import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""

    def test_valid_vertical_move(self):
        """Verifica que la torre se pueda mover verticalmente"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        self.assertTrue(rook.is_valid_piece_move(self.board, (0, 0), (5, 0)))  
        """Movimiento vertical"""

    def test_valid_horizontal_move(self):
        """Verifica que la torre se pueda mover horizontalmente"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        self.assertTrue(rook.is_valid_piece_move(self.board, (0, 0), (0, 7)))  
        """Movimiento horizontal"""

    def test_invalid_diagonal_move(self):
        """Verifica que la torre no se pueda mover en diagonal"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        self.assertFalse(rook.is_valid_piece_move(self.board, (0, 0), (3, 3)))  
        """Movimiento diagonal"""

    def test_blocked_move(self):
        """Verifica que la torre no pueda atravesar otras piezas"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        blocking_piece = Rook("WHITE", (3, 0))
        self.board.set_piece(3, 0, blocking_piece)
        self.assertFalse(rook.is_valid_piece_move(self.board, (0, 0), (5, 0)))  
        """Camino bloqueado"""

    def test_capture_enemy_piece(self):
        """Verifica que la torre pueda capturar una pieza enemiga"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        enemy_piece = Rook("BLACK", (5, 0))
        self.board.set_piece(5, 0, enemy_piece)
        self.assertTrue(rook.is_valid_piece_move(self.board, (0, 0), (5, 0)))  
        """Captura de pieza enemiga"""

    def test_capture_own_piece(self):
        """Verifica que la torre no pueda capturar una pieza propia"""
        rook = Rook("WHITE", (0, 0))
        self.board.set_piece(0, 0, rook)
        own_piece = Rook("WHITE", (5, 0))
        self.board.set_piece(5, 0, own_piece)
        self.assertFalse(rook.is_valid_piece_move(self.board, (0, 0), (5, 0)))  
        """No puede capturar pieza propia"""

if __name__ == '__main__':
    unittest.main()
