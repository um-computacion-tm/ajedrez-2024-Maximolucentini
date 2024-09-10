import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from game.board import Board
from game.piece import Piece
from game.rook import Rook
from game.pawn import Pawn




class TestRook(unittest.TestCase):

    def setUp(self):
        """Crear un tablero para los tests"""
        self.board = Board()
        
        """Limpiar el tablero de peones para evitar bloqueos"""
        for col in range(8):
            self.board.set_piece(6, col, None)  
            """Limpiar peones blancos"""
            self.board.set_piece(1, col, None)  
            """Limpiar peones negros"""

    def test_horizontal_move_left(self):
        """Test para movimiento horizontal válido hacia la izquierda"""
        rook = self.board.get_piece(7, 7)  
        """Torre blanca en (7, 7)"""
        self.assertTrue(rook.is_valid_move(self.board, 7, 7, 7, 3))  
        """Mover horizontalmente a (7, 3)"""

    def test_horizontal_move_right(self):
        """Test para movimiento horizontal válido hacia la derecha"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.assertTrue(rook.is_valid_move(self.board, 7, 0, 7, 5))  
        """Mover horizontalmente a (7, 5)"""

    def test_vertical_move_down(self):
        """Test para movimiento vertical válido hacia abajo"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.assertTrue(rook.is_valid_move(self.board, 7, 0, 4, 0))  
        """Mover verticalmente a (4, 0)"""

    def test_vertical_move_up(self):
        """Test para movimiento vertical válido hacia arriba"""
        rook = self.board.get_piece(7, 7)  
        """Torre blanca en (7, 7)"""
        self.assertTrue(rook.is_valid_move(self.board, 7, 7, 3, 7))  
        """Mover verticalmente a (3, 7)"""
        
    def test_blocked_move_horizontal(self):
        """Test para un movimiento horizontal bloqueado"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.board.set_piece(7, 3, Pawn("WHITE", position=(7, 3)))  
        """Colocar un peón blanco para bloquear"""
        self.assertFalse(rook.is_valid_move(self.board, 7, 0, 7, 5))  
        """Intentar moverse más allá del peón"""

    def test_blocked_move_vertical(self):
        """Test para un movimiento vertical bloqueado"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.board.set_piece(5, 0, Pawn("WHITE", position=(5, 0)))  
        """Colocar un peón blanco para bloquear"""
        self.assertFalse(rook.is_valid_move(self.board, 7, 0, 4, 0))  
        """Intentar moverse más allá del peón"""

    def test_capture_move(self):
        """Test para un movimiento de captura válido"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.board.set_piece(7, 5, Pawn("BLACK", position=(7, 5)))  
        """Colocar un peón negro en la línea de captura"""
        self.assertTrue(rook.is_valid_move(self.board, 7, 0, 7, 5))  
        """Moverse y capturar"""

    def test_invalid_diagonal_move(self):
        """Test para un movimiento inválido en diagonal"""
        rook = self.board.get_piece(7, 0)  
        """Torre blanca en (7, 0)"""
        self.assertFalse(rook.is_valid_move(self.board, 7, 0, 5, 2))  
        """Intentar moverse en diagonal (movimiento no permitido)"""
        

    
        
if __name__ == '__main__':    
    unittest.main()
        