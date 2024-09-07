import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.piece import Piece
from game.board import Board
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        # Crear un tablero para los tests
        self.board = Board()
        
    def test_initial_two_square_move(self):
        """Test para el movimiento inicial de dos casillas hacia adelante"""
        white_pawn = self.board.get_piece(6, 0)
        self.assertTrue(white_pawn.is_valid_move(self.board, 6, 0, 4, 0))
        
        black_pawn = self.board.get_piece(1, 0)
        self.assertTrue(black_pawn.is_valid_move(self.board, 1, 0, 3, 0))

    def test_one_square_move(self):
        """Test para el movimiento normal de una casilla hacia adelante"""
        white_pawn = self.board.get_piece(6, 0)
        self.board.move_piece(6, 0, 5, 0)
        self.assertTrue(white_pawn.is_valid_move(self.board, 5, 0, 4, 0))

        black_pawn = self.board.get_piece(1, 0)
        self.board.move_piece(1, 0, 2, 0)
        self.assertTrue(black_pawn.is_valid_move(self.board, 2, 0, 3, 0))

    def test_invalid_move(self):
        """Test para un movimiento inválido (mover en diagonal sin captura)"""
        white_pawn = self.board.get_piece(6, 0)
        self.assertFalse(white_pawn.is_valid_move(self.board, 6, 0, 5, 1))

    def test_capture(self):
        """Test para un movimiento de captura válido"""
        white_pawn = self.board.get_piece(6, 0)
        black_pawn = self.board.get_piece(1, 1)
        
        # Colocar un peón negro en una posición para ser capturado
        self.board.set_piece(5, 1, black_pawn)
        self.assertTrue(white_pawn.is_valid_move(self.board, 6, 0, 5, 1))

    def test_blocked_move(self):
        """Test para movimiento bloqueado por otra pieza"""
        white_pawn = self.board.get_piece(6, 0)
        black_pawn = self.board.get_piece(1, 0)

        # Colocar el peón negro frente al peón blanco para bloquearlo
        self.board.set_piece(5, 0, black_pawn)
        self.assertFalse(white_pawn.is_valid_move(self.board, 6, 0, 5, 0))
    
if __name__ == '__main__':    
    unittest.main()
