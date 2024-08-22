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

class TestBoardSetup(unittest.TestCase):
    
    def setUp(self):
        self.__board__ = Board()

    def test_initial_piece_positions(self):
        # Verificar las posiciones iniciales de las piezas
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(0, 1), Knight)
        self.assertIsInstance(self.__board__.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.__board__.get_piece(0, 3), Queen)
        self.assertIsInstance(self.__board__.get_piece(0, 4), King)
        self.assertIsInstance(self.__board__.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.__board__.get_piece(0, 6), Knight)
        self.assertIsInstance(self.__board__.get_piece(0, 7), Rook)

        self.assertIsInstance(self.__board__.get_piece(7, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(7, 1), Knight)
        self.assertIsInstance(self.__board__.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.__board__.get_piece(7, 3), Queen)
        self.assertIsInstance(self.__board__.get_piece(7, 4), King)
        self.assertIsInstance(self.__board__.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.__board__.get_piece(7, 6), Knight)
        self.assertIsInstance(self.__board__.get_piece(7, 7), Rook)

        # Verificar las posiciones iniciales de los peones
        for col in range(8):
            self.assertIsInstance(self.__board__.get_piece(1, col), Pawn)
            self.assertIsInstance(self.__board__.get_piece(6, col), Pawn)
            
class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.__board__ = Board()

    
    def test_move_piece_valid(self):
        # Mover un peón blanco desde la posición inicial (6, 0) a (5, 0)
        self.__board__.move_piece(6, 0, 5, 0)
        move_piece = self.__board__.get_piece(5, 0)
        self.assertIsNotNone(move_piece)
        self.assertEqual(move_piece.__color__, "WHITE")
        self.assertEqual(move_piece.__position__, (5, 0))
        
        # Asegurarse de que la posición inicial esté vacía
        self.assertIsNone(self.__board__.get_piece(6, 0))

    def test_move_piece_invalid(self):
        # Intento de mover un peón blanco de manera inválida
        with self.assertRaises(ValueError):
            self.__board__.move_piece(6, 0, 4, 0)  # Movimiento inválido, ya que debería moverse de a una casilla
            
    def test_get_piece(self):
        """Verifica que get_piece devuelve la pieza correcta en una posición dada."""
        piece = self.__board__.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.__color__, "BLACK")

        piece = self.__board__.get_piece(1, 0)
        self.assertIsInstance(piece, Pawn)
        self.assertEqual(piece.__color__, "BLACK")

        piece = self.__board__.get_piece(7, 7)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.__color__, "WHITE")
        
    def test_show_board(self):
        # Verificar que el tablero se muestra correctamente
        board_str = self.__board__.show_board()
        expected_row1 = "r . . . . . . r\n"  # Filas con torres negras
        expected_row2 = "p p p p p p p p\n"  # Filas con peones negros
        expected_empty = ". . . . . . . .\n"  # Filas vacías
        expected_row7 = "P P P P P P P P\n"  # Filas con peones blancos
        expected_row8 = "R . . . . . . R\n"  # Filas con torres blancas
        
        self.assertIn(expected_row1, board_str)
        self.assertIn(expected_row2, board_str)
        self.assertIn(expected_empty, board_str)
        self.assertIn(expected_row7, board_str)
        self.assertIn(expected_row8, board_str)

if __name__ == '__main__':
    unittest.main()
