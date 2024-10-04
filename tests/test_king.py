import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.king import King
from game.piece import Piece

class TestKing(unittest.TestCase):

    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""

    def test_valid_move(self):
        """Verifica que el rey pueda moverse una casilla en cualquier dirección"""
        king = King("WHITE", (4, 4))
        self.board.set_piece(4, 4, king)
        self.assertTrue(king.is_valid_piece_move(self.board, (4, 4), (5, 5)))  
        """Movimiento diagonal"""
        self.assertTrue(king.is_valid_piece_move(self.board, (4, 4), (4, 5)))  
        """Movimiento horizontal"""
        self.assertTrue(king.is_valid_piece_move(self.board, (4, 4), (5, 4)))  
        """Movimiento vertical"""

    def test_invalid_move(self):
        """Verifica que el rey no pueda moverse más de una casilla en cualquier dirección"""
        king = King("WHITE", (4, 4))
        self.board.set_piece(4, 4, king)
        self.assertFalse(king.is_valid_piece_move(self.board, (4, 4), (6, 4)))  
        """Movimiento inválido (2 casillas vertical)"""
        self.assertFalse(king.is_valid_piece_move(self.board, (4, 4), (4, 6)))  
        """Movimiento inválido (2 casillas horizontal)"""
        self.assertFalse(king.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """Movimiento inválido (2 casillas diagonal)"""

    def test_capture_enemy_piece(self):
        """Verifica que el rey pueda capturar una pieza enemiga"""
        king = King("WHITE", (4, 4))
        self.board.set_piece(4, 4, king)
        enemy_piece = King("BLACK", (5, 5))
        self.board.set_piece(5, 5, enemy_piece)
        self.assertTrue(king.is_valid_piece_move(self.board, (4, 4), (5, 5)))  
        """Captura de pieza enemiga"""

    def test_capture_own_piece(self):
        """Verifica que el rey no pueda capturar una pieza propia"""
        king = King("WHITE", (4, 4))
        self.board.set_piece(4, 4, king)
        own_piece = King("WHITE", (5, 5))
        self.board.set_piece(5, 5, own_piece)
        self.assertFalse(king.is_valid_piece_move(self.board, (4, 4), (5, 5)))  
        """No puede capturar pieza propia"""

    def test_symbol(self):
        """Verifica que el símbolo del rey sea correcto para ambos colores"""
        white_king = King("WHITE", (0, 4))
        black_king = King("BLACK", (7, 4))
        self.assertEqual(white_king.symbol(), 'K')  
        """Rey blanco"""
        self.assertEqual(black_king.symbol(), 'k')  
        """Rey negro"""

if __name__ == '__main__':
    unittest.main()
