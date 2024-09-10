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
        # Crear un tablero para los tests
        self.board = Board()

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
        
if __name__ == '__main__':    
    unittest.main()
        