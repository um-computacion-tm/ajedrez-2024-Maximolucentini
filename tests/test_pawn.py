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

   def test_pawn_move_one_square_forward(self):
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

   def test_pawn_capture_diagonal(self):
    """Prueba que el peón capture una pieza enemiga en diagonal."""
    """Mover peón negro adelante para permitir captura"""
    self.board.move_piece(1, 1, 3, 1)
    
    """Mueve el peón blanco en diagonal para capturar el peón negro"""
    pawn = self.board.get_piece(6, 0)
    self.board.move_piece(6, 0, 4, 0)
    self.assertTrue(pawn.is_valid_piece_move(self.board, (4, 0), (3, 1)))

   def test_pawn_invalid_move(self):
    """Prueba que un movimiento inválido no sea permitido."""
    pawn = self.board.get_piece(1, 0)
    
    """Movimiento inválido: diagonal sin captura"""
    self.assertFalse(pawn.is_valid_piece_move(self.board, (1, 0), (2, 1)))
    
    """Movimiento inválido: hacia atrás"""
    self.assertFalse(pawn.is_valid_piece_move(self.board, (1, 0), (0, 0)))


        
        
        
if __name__ == '__main__':
 unittest.main()    