import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import *
from game.rook import *
from game.knight import *
from game.bishop import *
from game.queen import *
from game.king import *
from game.pawn import *
from game.piece import *

class TestBoard(unittest.TestCase):
  def test_init(self):
    board = Board()
    self.assertEqual(len(board.__positions__), 8)
    self.assertEqual(len(board.__positions__[0]), 8)
    """Verificar que la board esté configurada correctamente"""
    for row in range(8):
        for col in range(8):
            if row == 1 or row == 6:
                self.assertIsInstance(board.__positions__[row][col], Pawn)
            elif (row, col) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                self.assertIsInstance(board.__positions__[row][col], Rook)
            elif (row, col) in [(0, 1), (0, 6), (7, 1), (7, 6)]:
                self.assertIsInstance(board.__positions__[row][col], Knight)
            elif (row, col) in [(0, 2), (0, 5), (7, 2), (7, 5)]:
                self.assertIsInstance(board.__positions__[row][col], Bishop)
            elif (row, col) == (0, 3):
                self.assertIsInstance(board.__positions__[row][col], Queen)
            elif (row, col) == (7, 3):
                self.assertIsInstance(board.__positions__[row][col], Queen)
            elif (row, col) == (0, 4):
                self.assertIsInstance(board.__positions__[row][col], King)
            elif (row, col) == (7, 4):
                self.assertIsInstance(board.__positions__[row][col], King)
            else:
                self.assertIsNone(board.__positions__[row][col])
                
  def test_get_piece(self):
        board = Board()
        """ Verificar que se devuelva None para una posición vacía"""
        self.assertIsNone(board.get_piece(3, 3))
        """ Verificar que se devuelva una pieza para una posición ocupada"""
        piece = board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        
  def test_move_piece(self):
    board = Board()
    """ Verificar que el movimiento sea válido antes de intentar realizarlo"""
    piece = board.__positions__[1][0]
    self.assertIsInstance(piece, Pawn)
    self.assertTrue(board.is_valid_move(1, 0, 2, 0))
    """ Intentar mover la pieza"""
    board.move_piece(1, 0, 2, 0)
    """ Verificar que la pieza se haya movido correctamente"""
    self.assertIsNone(board.__positions__[1][0])
    self.assertIsInstance(board.__positions__[2][0], Pawn)
if __name__ == '__main__':
    unittest.main()
