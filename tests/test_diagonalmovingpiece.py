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
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Movimiento válido"""
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_invalid_diagonal_move(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Movimiento no diagonal"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (2, 5)))

    def test_blocked_diagonal_move(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Bloqueamos el camino"""
        blocking_piece = DiagonalMovingPiece("BLACK", (3, 3))
        self.board.set_piece(3, 3, blocking_piece)
        """Movimiento obstruido"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_capture_enemy_piece(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Colocamos una pieza enemiga en el destino"""
        enemy_piece = DiagonalMovingPiece("BLACK", (4, 4))
        self.board.set_piece(4, 4, enemy_piece)
        """Movimiento de captura válido"""
        self.assertTrue(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

    def test_capture_own_piece(self):
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.board.set_piece(2, 2, piece)
        """Colocamos una pieza propia en el destino"""
        own_piece = DiagonalMovingPiece("WHITE", (4, 4))
        self.board.set_piece(4, 4, own_piece)
        """No puede capturar su propia pieza"""
        self.assertFalse(piece.is_valid_piece_move(self.board, (2, 2), (4, 4)))

if __name__ == '__main__':
    unittest.main()