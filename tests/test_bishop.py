import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.bishop import Bishop
from game.piece import Piece

class TestBishop(unittest.TestCase):

    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""

    def test_valid_diagonal_move(self):
        """Verifica que el alfil pueda moverse en diagonal"""
        bishop = Bishop("WHITE", (4, 4))
        self.board.set_piece(4, 4, bishop)
        self.assertTrue(bishop.is_valid_piece_move(self.board, (4, 4), (7, 7)))  
        """Movimiento diagonal"""

    def test_blocked_move(self):
        """Verifica que el alfil no pueda atravesar otras piezas"""
        bishop = Bishop("WHITE", (4, 4))
        self.board.set_piece(4, 4, bishop)
        blocking_piece = Bishop("WHITE", (6, 6))
        self.board.set_piece(6, 6, blocking_piece)
        self.assertFalse(bishop.is_valid_piece_move(self.board, (4, 4), (7, 7)))  
        """Camino bloqueado"""

    def test_capture_enemy_piece(self):
        """Verifica que el alfil pueda capturar una pieza enemiga"""
        bishop = Bishop("WHITE", (4, 4))
        self.board.set_piece(4, 4, bishop)
        enemy_piece = Bishop("BLACK", (6, 6))
        self.board.set_piece(6, 6, enemy_piece)
        self.assertTrue(bishop.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """Captura de pieza enemiga"""

    def test_capture_own_piece(self):
        """Verifica que el alfil no pueda capturar una pieza propia"""
        bishop = Bishop("WHITE", (4, 4))
        self.board.set_piece(4, 4, bishop)
        own_piece = Bishop("WHITE", (6, 6))
        self.board.set_piece(6, 6, own_piece)
        self.assertFalse(bishop.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """No puede capturar pieza propia"""

    def test_invalid_move(self):
        """Verifica que el alfil no pueda moverse de manera no diagonal"""
        bishop = Bishop("WHITE", (4, 4))
        self.board.set_piece(4, 4, bishop)
        self.assertFalse(bishop.is_valid_piece_move(self.board, (4, 4), (4, 7)))  
        """Movimiento no diagonal"""

    def test_symbol(self):
        """Verifica que el símbolo del alfil sea correcto para ambos colores"""
        white_bishop = Bishop("WHITE", (0, 2))
        black_bishop = Bishop("BLACK", (7, 2))
        self.assertEqual(white_bishop.symbol(), 'B')  
        """Alfil blanco"""
        self.assertEqual(black_bishop.symbol(), 'b')  
        """Alfil negro"""

if __name__ == '__main__':
    unittest.main()

    




if __name__ == '__main__':
    unittest.main()
