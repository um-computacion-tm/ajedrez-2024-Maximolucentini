import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""

    def test_valid_straight_move(self):
        """Verifica que la reina pueda moverse en línea recta (horizontal, vertical)"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        self.assertTrue(queen.is_valid_piece_move(self.board, (4, 4), (4, 7)))  
        """Movimiento horizontal"""
        self.assertTrue(queen.is_valid_piece_move(self.board, (4, 4), (7, 4)))  
        """Movimiento vertical"""

    def test_valid_diagonal_move(self):
        """Verifica que la reina pueda moverse en diagonal"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        self.assertTrue(queen.is_valid_piece_move(self.board, (4, 4), (7, 7)))  
        """Movimiento diagonal"""
        self.assertTrue(queen.is_valid_piece_move(self.board, (4, 4), (1, 1)))  
        """Movimiento diagonal inverso"""

    def test_blocked_move(self):
        """Verifica que la reina no pueda atravesar otras piezas"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        blocking_piece = Queen("WHITE", (6, 6))
        self.board.set_piece(6, 6, blocking_piece)
        self.assertFalse(queen.is_valid_piece_move(self.board, (4, 4), (7, 7)))  
        """Camino bloqueado"""

    def test_capture_enemy_piece(self):
        """Verifica que la reina pueda capturar una pieza enemiga"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        enemy_piece = Queen("BLACK", (6, 6))
        self.board.set_piece(6, 6, enemy_piece)
        self.assertTrue(queen.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """Captura de pieza enemiga"""

    def test_capture_own_piece(self):
        """Verifica que la reina no pueda capturar una pieza propia"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        own_piece = Queen("WHITE", (6, 6))
        self.board.set_piece(6, 6, own_piece)
        self.assertFalse(queen.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """No puede capturar pieza propia"""

    def test_invalid_move(self):
        """Verifica que la reina no pueda moverse fuera de los patrones válidos"""
        queen = Queen("WHITE", (4, 4))
        self.board.set_piece(4, 4, queen)
        self.assertFalse(queen.is_valid_piece_move(self.board, (4, 4), (5, 6)))  
        """Movimiento inválido (no recto ni diagonal)"""
        
    def test_symbol(self):
        """Verifica que el símbolo de la reina sea correcto para ambos colores"""
        white_queen = Queen("WHITE", (0, 3))
        black_queen = Queen("BLACK", (7, 3))
        self.assertEqual(white_queen.symbol(), 'Q')  
        """Reina blanca"""
        self.assertEqual(black_queen.symbol(), 'q')  
        """Reina negra"""
    

if __name__ == '__main__':
    unittest.main()
