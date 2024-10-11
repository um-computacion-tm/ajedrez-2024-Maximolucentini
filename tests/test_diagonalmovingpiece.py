import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.diagonalmovingpiece import DiagonalMovingPiece
from game.piece import Piece

class TestDiagonalMovingPiece(unittest.TestCase):

    def setUp(self):
        """
        Creates an empty board for testing.
        """
        self.__board__ = Board()

    def test_valid_diagonal_move(self):
        """
        Ensures that a diagonal-moving piece can move diagonally.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        """Valid diagonal move"""
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))

    def test_invalid_diagonal_move(self):
        """
        Ensures that a diagonal-moving piece cannot move in a straight line.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        """"Invalid straight-line move"""
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 5)))

    def test_blocked_diagonal_move(self):
        """
        Ensures that a diagonal-moving piece cannot move if there is a piece blocking the path.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        """Block the path"""
        blocking_piece = DiagonalMovingPiece("BLACK", (3, 3))
        self.__board__.set_piece(3, 3, blocking_piece)
        """Path is blocked"""
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))

    def test_capture_enemy_piece(self):
        """
        Ensures that a diagonal-moving piece can capture an enemy piece.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        """Place an enemy piece at the destination"""
        enemy_piece = DiagonalMovingPiece("BLACK", (4, 4))
        self.__board__.set_piece(4, 4, enemy_piece)
        """Valid capture move"""
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))

    def test_capture_own_piece(self):
        """
        Ensures that a diagonal-moving piece cannot capture its own piece.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        """Place an own piece at the destination"""
        own_piece = DiagonalMovingPiece("WHITE", (4, 4))
        self.__board__.set_piece(4, 4, own_piece)
        """Cannot capture own piece"""
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))

    def test_move_out_of_board(self):
        """
        Ensures that a diagonal-moving piece cannot move outside the board.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (8, 8)))  
        """Out of bounds"""

    def test_valid_diagonal_move_without_capture(self):
        """
        Ensures that a diagonal-moving piece can move diagonally without capturing.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))  
        """No pieces in the way or destination"""

    def test_valid_diagonal_move_up_right(self):
        """
        Ensures that a diagonal-moving piece can move diagonally up-right.
        """
        piece = DiagonalMovingPiece("WHITE", (5, 5))
        self.__board__.set_piece(5, 5, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (5, 5), (3, 7)))  
        """Move up-right"""

    def test_valid_diagonal_move_up_left(self):
        """
        Ensures that a diagonal-moving piece can move diagonally up-left.
        """
        piece = DiagonalMovingPiece("WHITE", (5, 5))
        self.__board__.set_piece(5, 5, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (5, 5), (3, 3)))  
        """Move up-left"""

    def test_valid_diagonal_move_down_right(self):
        """
        Ensures that a diagonal-moving piece can move diagonally down-right.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (2, 2), (4, 4)))  
        """Move down-right"""

    def test_valid_diagonal_move_down_left(self):
        """
        Ensures that a diagonal-moving piece can move diagonally down-left.
        """
        """Create an empty board to avoid conflicts with standard setup"""
        self.__board__ = Board()
        self.__board__.__positions__ = [[None for _ in range(8)] for _ in range(8)]  
        """Empty board"""
    
        piece = DiagonalMovingPiece("WHITE", (5, 5))  
        """Place the piece at (5, 5)"""
        self.__board__.set_piece(5, 5, piece)
    
        """Valid move down-left"""
        self.assertTrue(piece.is_valid_piece_move(self.__board__, (5, 5), (7, 3)))

    def test_move_to_same_position(self):
        """
        Ensures that a diagonal-moving piece cannot move to the same position.
        """
        piece = DiagonalMovingPiece("WHITE", (2, 2))
        self.__board__.set_piece(2, 2, piece)
        self.assertFalse(piece.is_valid_piece_move(self.__board__, (2, 2), (2, 2)))  
        """Same position"""

if __name__ == '__main__':
    unittest.main()
