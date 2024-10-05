import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.board import Board
from game.pawn import Pawn
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        """Configura un tablero antes de cada prueba."""
        self.board = Board()

    def test_initial_setup(self):
        """Verifica que el tablero esté correctamente configurado al iniciar."""
        """Verificar peones en sus posiciones iniciales"""
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertEqual(self.board.get_piece(1, col).get_color(), "BLACK")
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)
            self.assertEqual(self.board.get_piece(6, col).get_color(), "WHITE")

        """Verificar torres en sus posiciones iniciales"""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color(), "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color(), "WHITE")

    def test_get_piece(self):
        """Prueba el método get_piece en diferentes posiciones."""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        """Una celda vacía debería devolver None"""
        self.assertIsNone(self.board.get_piece(3, 3))

    def test_set_piece(self):
        """Prueba el método set_piece para colocar una pieza en una posición específica."""
        rook = Rook("WHITE")
        self.board.set_piece(3, 3, rook)
        self.assertIs(self.board.get_piece(3, 3), rook)

    def test_is_valid_move(self):
        """Prueba algunos movimientos válidos e inválidos."""
        """Antes de mover el peón, su estado inicial debería ser True"""
        pawn = self.board.get_piece(6, 0)

        """Mover una casilla debe ser válido"""
        self.assertTrue(self.board.is_valid_move(6, 0, 5, 0))  
        """peón blanco en 6,0 a 5,0"""

        """Después de mover, su estado inicial debería ser False"""
        self.board.move_piece(6, 0, 5, 0)

        """Ahora mover dos casillas debe ser inválido"""
        self.assertFalse(self.board.is_valid_move(5, 0, 3, 0))  
        """peón blanco no puede moverse dos posiciones en este caso"""

    def test_move_piece(self):
        """Prueba que una pieza se mueva correctamente en el tablero."""
        """Mover un peón blanco hacia adelante"""
        self.board.move_piece(6, 0, 5, 0)  
        """peón de 6,0 a 5,0"""
        self.assertIsInstance(self.board.get_piece(5, 0), Pawn)
        """La posición original debe quedar vacía"""
        self.assertIsNone(self.board.get_piece(6, 0))
        
    def test_invalid_move(self):
        """Prueba que un movimiento inválido genere un ValueError."""
        """Intentar mover desde una posición vacía"""
        with self.assertRaises(ValueError):
            self.board.move_piece(3, 3, 4, 3)

        """Intentar mover a una casilla ocupada por una pieza del mismo color"""
        with self.assertRaises(ValueError):
            self.board.move_piece(0, 0, 0, 1)  
            """torre negra no puede moverse a donde está el caballo negro"""

    def test_show_board(self):
        """Verifica que el método show_board devuelva una representación del tablero."""
        board_str = self.board.show_board()
        self.assertIsInstance(board_str, str)
        """Verificar que la representación contenga 8 filas"""
        self.assertEqual(len(board_str.strip().split("\n")), 8)

    def test_pawn_initial_position(self):
        """Prueba que el peón actualice correctamente su estado initial_position después del primer movimiento."""
        """Mover el peón por primera vez"""
        self.board.move_piece(6, 0, 4, 0)

        """Verificar que el peón ya no esté en su posición inicial"""
        pawn = self.board.get_piece(4, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertFalse(pawn.initial_position)  
        """Debe ser False después del movimiento"""

        """Intentar moverlo dos casillas nuevamente debe ser inválido"""
        self.assertFalse(self.board.is_valid_move(4, 0, 2, 0))  
        """No debería poder moverse dos casillas"""    
        
    def test_get_pieces_in_row(self):
        """Verifica que se devuelvan las piezas de un color en una fila"""
        white_pieces_row_6 = self.board.get_pieces_in_row(6, "WHITE")
        self.assertEqual(len(white_pieces_row_6), 8)  
        """Hay 8 peones blancos en la fila 6"""
        self.assertTrue(all(piece.get_color() == "WHITE" for piece in white_pieces_row_6))

        black_pieces_row_1 = self.board.get_pieces_in_row(1, "BLACK")
        self.assertEqual(len(black_pieces_row_1), 8)  
        """Hay 8 peones negros en la fila 1"""
        self.assertTrue(all(piece.get_color() == "BLACK" for piece in black_pieces_row_1))

    def test_get_pieces(self):
        """Verifica que se devuelvan todas las piezas de un color en el tablero"""
        white_pieces = self.board.get_pieces("WHITE")
        self.assertEqual(len(white_pieces), 16)  
        """Hay 16 piezas blancas en el tablero"""
        self.assertTrue(all(piece.get_color() == "WHITE" for piece in white_pieces))

        black_pieces = self.board.get_pieces("BLACK")
        self.assertEqual(len(black_pieces), 16)  
        """Hay 16 piezas negras en el tablero"""
        self.assertTrue(all(piece.get_color() == "BLACK" for piece in black_pieces))    

if __name__ == '__main__':
 unittest.main()    