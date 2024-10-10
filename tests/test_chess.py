import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import unittest
from game.chess import Chess
from game.board import Board
from game.pawn import Pawn
from game.king import King

class TestChess(unittest.TestCase):
    def setUp(self):
        """Configura un juego de ajedrez antes de cada prueba"""
        self.chess_game = Chess()

    def test_initialize_pieces(self):
        """Verifica que las piezas estén correctamente posicionadas al inicio del juego"""
        board = self.chess_game.board

        # Verificar peones blancos
        for col in range(8):
            self.assertIsInstance(board.get_piece(6, col), Pawn)
            self.assertEqual(board.get_piece(6, col).get_color(), "WHITE")

        # Verificar peones negros
        for col in range(8):
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertEqual(board.get_piece(1, col).get_color(), "BLACK")

        # Verificar reyes
        self.assertIsInstance(board.get_piece(7, 4), King)
        self.assertEqual(board.get_piece(7, 4).get_color(), "WHITE")
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertEqual(board.get_piece(0, 4).get_color(), "BLACK")

    def test_switch_turn(self):
        """Prueba que los turnos alternen correctamente"""
        self.assertEqual(self.chess_game.current_turn, "WHITE")
        self.chess_game.switch_turn()
        self.assertEqual(self.chess_game.current_turn, "BLACK")
        self.chess_game.switch_turn()
        self.assertEqual(self.chess_game.current_turn, "WHITE")

    def test_is_valid_turn(self):
        """Verifica si se está moviendo la pieza del jugador correcto"""
        board = self.chess_game.board
        white_pawn = board.get_piece(6, 0)
        black_pawn = board.get_piece(1, 0)

        self.assertTrue(self.chess_game.is_valid_turn(white_pawn))  # Turno blanco
        self.chess_game.switch_turn()
        self.assertTrue(self.chess_game.is_valid_turn(black_pawn))  # Turno negro

    def test_make_move_valid(self):
        """Prueba que un movimiento válido se ejecute correctamente"""
        result, message = self.chess_game.make_move((6, 0), (5, 0))  # Mover un peón blanco hacia adelante
        self.assertTrue(result)
        self.assertEqual(message, "WHITE ♙ se movió de (6, 0) a (5, 0)")
        self.assertIsInstance(self.chess_game.board.get_piece(5, 0), Pawn)
        self.assertIsNone(self.chess_game.board.get_piece(6, 0))

    def test_make_move_invalid(self):
        """Prueba que un movimiento inválido no se ejecute"""
        # Mover el peón blanco desde a2 a a4 (movimiento válido)
        result, message = self.chess_game.make_move((6, 0), (4, 0))
        self.assertTrue(result)

        # Cambiar de turno para mover una pieza negra y luego intentar un movimiento inválido
        self.chess_game.switch_turn()

        # Intentar mover el mismo peón blanco desde a4 a a6 (movimiento inválido)
        result, message = self.chess_game.make_move((4, 0), (2, 0))  # Movimiento inválido
        self.assertFalse(result)
        self.assertEqual(message, "Movimiento inválido.")


    def test_end_game_by_agreement(self):
        """Prueba que el juego pueda finalizar por acuerdo mutuo"""
        self.chess_game.end_game_by_agreement()
        self.assertTrue(self.chess_game.is_game_over)

    def test_check_end_conditions(self):
     """Prueba las condiciones de final de juego (cuando un jugador se queda sin piezas)"""
     # Eliminar todas las piezas negras
     for i in range(8):
        self.chess_game.board.set_piece(1, i, None)  # Elimina los peones negros
     # Eliminar el resto de piezas negras
     self.chess_game.board.set_piece(0, 0, None)  # Torre negra
     self.chess_game.board.set_piece(0, 1, None)  # Caballo negro
     self.chess_game.board.set_piece(0, 2, None)  # Alfil negro
     self.chess_game.board.set_piece(0, 3, None)  # Reina negra
     self.chess_game.board.set_piece(0, 4, None)  # Rey negro
     self.chess_game.board.set_piece(0, 5, None)  # Alfil negro
     self.chess_game.board.set_piece(0, 6, None)  # Caballo negro
     self.chess_game.board.set_piece(0, 7, None)  # Torre negra

     # Verificar que no quedan piezas negras
     black_pieces = self.chess_game.board.get_pieces("BLACK")
     self.assertEqual(len(black_pieces), 0)  # Confirmar que todas las piezas negras fueron eliminadas

     game_over, message = self.chess_game.check_end_conditions()
     self.assertTrue(game_over)
     self.assertEqual(message, "Las piezas negras han sido eliminadas. ¡Ganan las blancas!")

     # Eliminar todas las piezas blancas
     self.setUp()  # Reiniciar el juego
     for i in range(8):
        self.chess_game.board.set_piece(6, i, None)  # Elimina los peones blancos
     self.chess_game.board.set_piece(7, 0, None)  # Torre blanca
     self.chess_game.board.set_piece(7, 1, None)  # Caballo blanco
     self.chess_game.board.set_piece(7, 2, None)  # Alfil blanco
     self.chess_game.board.set_piece(7, 3, None)  # Reina blanca
     self.chess_game.board.set_piece(7, 4, None)  # Rey blanco
     self.chess_game.board.set_piece(7, 5, None)  # Alfil blanco
     self.chess_game.board.set_piece(7, 6, None)  # Caballo blanco
     self.chess_game.board.set_piece(7, 7, None)  # Torre blanca

     # Verificar que no quedan piezas blancas
     white_pieces = self.chess_game.board.get_pieces("WHITE")
     self.assertEqual(len(white_pieces), 0)  # Confirmar que todas las piezas blancas fueron eliminadas

     game_over, message = self.chess_game.check_end_conditions()
     self.assertTrue(game_over)
     self.assertEqual(message, "Las piezas blancas han sido eliminadas. ¡Ganan las negras!")

if __name__ == '__main__':
    unittest.main()
