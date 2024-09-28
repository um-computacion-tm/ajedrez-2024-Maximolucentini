import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.piece import Piece


"""Mock para el tablero"""
class MockBoard:
    def __init__(self, pieces=None):
        self.pieces = pieces if pieces else {}

    def get_piece(self, row, col):
        return self.pieces.get((row, col), None)

class TestPiece(unittest.TestCase):

    def setUp(self):
        """Configura una pieza y un mock de tablero antes de cada prueba."""
        self.piece = Piece("WHITE", (0, 0))  
        """Creamos una pieza blanca en la posición (0, 0)"""
        self.board = MockBoard()  
        """Creamos un mock del tablero sin piezas"""

    def test_get_color(self):
        """Prueba que get_color devuelva el color correcto."""
        self.assertEqual(self.piece.get_color(), "WHITE")

    def test_get_position(self):
        """Prueba que get_position devuelva la posición correcta."""
        self.assertEqual(self.piece.get_position(), (0, 0))

    def test_set_position(self):
        """Prueba que set_position establezca correctamente la nueva posición."""
        self.piece.set_position((1, 1))
        self.assertEqual(self.piece.get_position(), (1, 1))

    def test_is_valid_destination_within_bounds(self):
        """Prueba que is_valid_destination devuelva True cuando la posición está dentro del tablero y no ocupada."""
        self.assertTrue(self.piece.is_valid_destination(self.board, 4, 4))

    def test_is_valid_destination_out_of_bounds(self):
        """Prueba que is_valid_destination devuelva False cuando la posición está fuera del tablero."""
        self.assertFalse(self.piece.is_valid_destination(self.board, 8, 8))  
        """Fuera del tablero"""

    def test_is_valid_destination_occupied_by_same_color(self):
        """Prueba que is_valid_destination devuelva False cuando la posición está ocupada por una pieza del mismo color."""
        """Agregar una pieza blanca en la posición (4, 4)"""
        self.board.pieces[(4, 4)] = Piece("WHITE", (4, 4))
        self.assertFalse(self.piece.is_valid_destination(self.board, 4, 4))

    def test_is_valid_destination_occupied_by_opponent(self):
        """Prueba que is_valid_destination devuelva True cuando la posición está ocupada por una pieza del color contrario."""
        """Agregar una pieza negra en la posición (4, 4)"""
        self.board.pieces[(4, 4)] = Piece("BLACK", (4, 4))
        self.assertTrue(self.piece.is_valid_destination(self.board, 4, 4))

    def test_move(self):
        """Prueba que move actualice correctamente la posición de la pieza."""
        self.piece.move(3, 3)
        self.assertEqual(self.piece.get_position(), (3, 3))

    def test_str(self):
        """Prueba la representación en cadena del objeto Piece."""
        self.assertEqual(str(self.piece), "WHITE Piece at (0, 0)")

if __name__ == '__main__':
    unittest.main()
