import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.bishop import Bishop
from game.piece import Piece

class TestBishop(unittest.TestCase):

    def setUp(self):
        """Configura un tablero real y un alfil antes de cada prueba."""
        self.board = Board()  
        """Usamos el tablero real"""
        self.bishop = Bishop("WHITE", (0, 2))  
        """Creamos un alfil blanco en la posición (0, 2)"""

    def test_symbol(self):
        """Prueba que el símbolo del alfil sea correcto."""
        self.assertEqual(self.bishop.symbol(), 'B')

        black_bishop = Bishop("BLACK", (7, 2))
        self.assertEqual(black_bishop.symbol(), 'b')


    def test_is_valid_piece_move_invalid(self):
        """Prueba que el alfil no pueda hacer movimientos no diagonales."""
        """Movimiento horizontal (no válido para el alfil)"""
        self.assertFalse(self.bishop.is_valid_piece_move(self.board, (0, 2), (0, 5)))

        """Movimiento vertical (no válido para el alfil)"""
        self.assertFalse(self.bishop.is_valid_piece_move(self.board, (0, 2), (3, 2)))

    def test_is_valid_piece_move_with_blocked_path(self):
        """Prueba que el alfil no pueda moverse si hay una pieza en el camino."""
        """Colocar una pieza en el camino"""
        blocking_piece = Piece("WHITE", (1, 3))
        self.board.set_piece(1, 3, blocking_piece)

        """El camino está bloqueado, el movimiento no debería ser válido"""
        self.assertFalse(self.bishop.is_valid_piece_move(self.board, (0, 2), (2, 4)))




if __name__ == '__main__':
    unittest.main()
