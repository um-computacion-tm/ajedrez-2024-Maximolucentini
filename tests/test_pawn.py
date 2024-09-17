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

    def test_pawn_move_forward(self):
        """Prueba que el peón se mueva una casilla hacia adelante."""
        pawn = self.board.get_piece(6, 0)
        """Prueba un movimiento válido de una casilla hacia adelante."""
        self.assertTrue(pawn.is_valid_piece_move(self.board, (6, 0), (5, 0)))

    def test_pawn_move_two_squares_from_initial(self):
        """Prueba que el peón se mueva dos casillas desde la posición inicial."""
        pawn = self.board.get_piece(6, 0)
        """Prueba un movimiento válido de dos casillas hacia adelante desde la posición inicial."""
        self.assertTrue(pawn.is_valid_piece_move(self.board, (6, 0), (4, 0)))
        
        """Después de moverse, no debería poder moverse otras dos casillas"""
        self.board.move_piece(6, 0, 4, 0)
        self.assertFalse(pawn.is_valid_piece_move(self.board, (4, 0), (2, 0)))

        
        
        
if __name__ == '__main__':
 unittest.main()    