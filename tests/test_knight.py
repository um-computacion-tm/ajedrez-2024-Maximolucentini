import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""

    def test_valid_knight_move(self):
        """Verifica que el caballo pueda moverse en forma de L"""
        knight = Knight("WHITE", (4, 4))
        self.board.set_piece(4, 4, knight)  
        """Pasar fila y columna separadas"""
        self.assertTrue(knight.is_valid_piece_move(self.board, (4, 4), (6, 5)))  
        """Movimiento válido (2, 1)"""
        self.assertTrue(knight.is_valid_piece_move(self.board, (4, 4), (2, 5)))  
        """Movimiento válido (2, -1)"""
        self.assertTrue(knight.is_valid_piece_move(self.board, (4, 4), (5, 6)))  
        """Movimiento válido (1, 2)"""
        self.assertTrue(knight.is_valid_piece_move(self.board, (4, 4), (5, 2)))  
        """Movimiento válido (1, -2)"""

    def test_invalid_knight_move(self):
        """Verifica que el caballo no se pueda mover de manera inválida (no en L)"""
        knight = Knight("WHITE", (4, 4))
        self.board.set_piece(4, 4, knight)
        """Pasar fila y columna separadas""" 
        self.assertFalse(knight.is_valid_piece_move(self.board, (4, 4), (4, 6)))  
        """Movimiento horizontal"""
        self.assertFalse(knight.is_valid_piece_move(self.board, (4, 4), (6, 6)))  
        """Movimiento diagonal"""

    def test_knight_capture_enemy_piece(self):
        """Verifica que el caballo pueda capturar una pieza enemiga"""
        knight = Knight("WHITE", (4, 4))
        self.board.set_piece(4, 4, knight)  
        """Pasar fila y columna separadas"""
        enemy_piece = Knight("BLACK", (6, 5))
        self.board.set_piece(6, 5, enemy_piece)  
        """Pasar fila y columna separadas"""
        self.assertTrue(knight.is_valid_piece_move(self.board, (4, 4), (6, 5)))  
        """Captura de pieza enemiga"""

    def test_knight_capture_own_piece(self):
        """Verifica que el caballo no pueda capturar una pieza propia"""
        knight = Knight("WHITE", (4, 4))
        self.board.set_piece(4, 4, knight)  
        """Pasar fila y columna separadas"""
        own_piece = Knight("WHITE", (6, 5))
        self.board.set_piece(6, 5, own_piece)  
        """Pasar fila y columna separadas"""
        self.assertFalse(knight.is_valid_piece_move(self.board, (4, 4), (6, 5)))  
        """No puede capturar su propia pieza"""

    def test_knight_move_out_of_board(self):
        """Verifica que el caballo no pueda moverse fuera del tablero"""
        knight = Knight("WHITE", (7, 7))
        self.board.set_piece(7, 7, knight)  
        """Pasar fila y columna separadas"""
        self.assertFalse(knight.is_valid_piece_move(self.board, (7, 7), (9, 8)))  
        """Movimiento fuera del tablero"""

if __name__ == '__main__':
    unittest.main()

