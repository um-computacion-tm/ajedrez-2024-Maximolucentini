import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.diagonalmovingpiece import DiagonalMovingPiece
from game.piece import Piece

class TestDiagonalMovingPiece(unittest.TestCase):

    def setUp(self):
        """Creamos un tablero vacío para las pruebas"""
        self.board = Board()

    def test_valid_diagonal_move(self):
        """Asegurar que un alfil pueda moverse en diagonal."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Movimiento válido"""
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_invalid_diagonal_move(self):
        """Asegurar que un alfil no pueda moverse en línea recta."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Movimiento no diagonal"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))

    def test_blocked_diagonal_move(self):
        """Asegurar que un alfil no pueda moverse si hay una pieza en el camino."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Bloqueamos el camino"""
        blocking_piece = DiagonalMovingPiece("BLACK", (3, 3))
        self.board.set_piece(3, 3, blocking_piece)
        """Movimiento obstruido"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_capture_enemy_piece(self):
        """Asegurar que un alfil pueda capturar una pieza enemiga."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Colocamos una pieza enemiga en el destino"""
        enemy_piece = DiagonalMovingPiece("BLACK", (4, 4))
        self.board.set_piece(4, 4, enemy_piece)
        """Movimiento de captura válido"""
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_capture_own_piece(self):
        """Asegurar que un alfil no pueda capturar su propia pieza."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Colocamos una pieza propia en el destino"""
        own_piece = DiagonalMovingPiece("WHITE", (4, 4))
        self.board.set_piece(4, 4, own_piece)
        """No puede capturar su propia pieza"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))
        
        
    
    def test_move_out_of_board(self):
        """Asegurar que un alfil no pueda moverse fuera del tablero."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (8, 8)))  
        """Fuera de los límites"""

    
    def test_valid_diagonal_move_without_capture(self):
        """Asegurar que un alfil pueda moverse en diagonal sin capturar."""
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))  
        """Sin piezas en el camino ni en el destino"""

    
    def test_valid_diagonal_move_up_right(self):
        """Asegurar que un alfil pueda moverse en diagonal hacia arriba a la derecha."""
        piece = DiagonalMovingPiece("WHITE", (5, 5))
        self.board.set_piece(5, 5, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (5, 5), (3, 7)))  
        """Movimiento arriba a la derecha"""

    def test_valid_diagonal_move_up_left(self):
        piece = DiagonalMovingPiece("WHITE", (5, 5))
        self.board.set_piece(5, 5, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (5, 5), (3, 3)))  
        """Movimiento arriba a la izquierda"""

    def test_valid_diagonal_move_down_right(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))  
        """Movimiento abajo a la derecha"""

    def test_valid_diagonal_move_down_left(self):
     """Asegurar que un alfil pueda moverse en diagonal hacia abajo a la izquierda."""
     """Crear un tablero vacío para evitar conflictos con la configuración estándar"""
     self.board = Board()
     self.board.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
     """Vaciar el tablero"""
    
     piece = DiagonalMovingPiece("WHITE", (5, 5))  
     """Colocar el alfil en (5, 5)"""
     self.board.set_piece(5, 5, piece)
    
     """Movimiento válido abajo-izquierda"""
     self.assertTrue(piece.is_valid_piece_move(self.board, (5, 5), (7, 3)))


    
    def test_move_to_same_position(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 2)))  
        """No puede moverse a la misma posición"""

if __name__ == '__main__':
    unittest.main()