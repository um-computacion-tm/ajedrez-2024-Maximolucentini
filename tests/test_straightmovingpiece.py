import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.straightmovingpiece import StraightMovingPiece
from game.piece import Piece

class TestStraightMovingPiece(unittest.TestCase):

    def setUp(self):
        """Creamos un tablero normal con la configuración inicial de ajedrez"""
        self.board = Board()

    def test_valid_horizontal_move(self):
        """Verifica un movimiento horizontal válido en un tablero vacío"""
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))  
        """Movimiento horizontal a la derecha"""
    
    def test_valid_vertical_move(self):
        """Verifica un movimiento vertical válido en un tablero vacío"""
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (5, 2)))  
        """Movimiento vertical hacia abajo"""
    
    def test_invalid_non_straight_move(self):
        """Verifica que un movimiento no recto sea inválido en un tablero vacío"""
        self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Tablero vacío"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (3, 3)))  
        """Movimiento diagonal"""
    
    def test_blocked_horizontal_move(self):
        """Verifica que un movimiento horizontal bloqueado sea inválido"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        blocking_piece = StraightMovingPiece("BLACK", (2, 4))
        self.board.set_piece(2, 4, blocking_piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))  
        """Camino bloqueado por pieza en (2, 4)"""
    
    def test_blocked_vertical_move(self):
        """Verifica que un movimiento vertical bloqueado sea inválido"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        blocking_piece = StraightMovingPiece("BLACK", (4, 2))
        self.board.set_piece(4, 2, blocking_piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (5, 2)))  
        """Camino bloqueado por pieza en (4, 2)"""
    
    def test_capture_enemy_piece(self):
        """Verifica que pueda capturar una pieza enemiga"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        enemy_piece = StraightMovingPiece("BLACK", (2, 5))
        self.board.set_piece(2, 5, enemy_piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))  
        """Captura de pieza enemiga"""
    
    def test_capture_own_piece(self):
        """Verifica que no pueda capturar una pieza propia"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        own_piece = StraightMovingPiece("WHITE", (2, 5))
        self.board.set_piece(2, 5, own_piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))  
        """No puede capturar pieza propia"""
    
    def test_move_out_of_board(self):
        """Verifica que no se pueda mover fuera del tablero"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (8, 2)))  
        """Fuera del límite vertical"""
    
    def test_move_to_same_position(self):
        """Verifica que no pueda moverse a la misma posición"""
        piece = StraightMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 2)))  
        """Mismo lugar"""

if __name__ == '__main__':
    unittest.main()
