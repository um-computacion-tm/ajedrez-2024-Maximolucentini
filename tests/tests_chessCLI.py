import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from game.chessCLI import ChessCLI

class TestChessCLI(unittest.TestCase):
    
    @patch('builtins.print')
    def test_display_board(self, mock_print):
        """Prueba que el tablero se imprima correctamente"""
        cli = ChessCLI()
        cli.display_board()
        # Verificar que el método print se llame con las posiciones correctas
        mock_print.assert_any_call("  a b c d e f g h")
        mock_print.assert_any_call(8, end=" ")
        mock_print.assert_any_call(1, end=" ")

    @patch('builtins.input', side_effect=['e2', 'e4'])  # Simula dos entradas
    @patch('builtins.print')
    def test_get_move_input(self, mock_print, mock_input):
        """Prueba que el movimiento ingresado por el jugador sea correcto"""
        cli = ChessCLI()
        from_pos, to_pos = cli.get_move_input()

        # Verificar que la entrada sea convertida correctamente
        self.assertEqual(from_pos, (6, 4))  # 'e2' -> (6, 4)
        self.assertEqual(to_pos, (4, 4))    # 'e4' -> (4, 4)

    @patch('builtins.input', side_effect=['n', 'e2', 'e4', 'n', 'e7', 'e5', 'n', 'g1', 'f3', 's'])  # Flujo con alternancia de turnos
    @patch('builtins.print')
    @patch('game.chess.Chess.make_move', return_value=(True, "Movimiento válido"))
    @patch('game.chess.Chess.check_end_conditions', return_value=(False, None))
    def test_play_game(self, mock_check_end_conditions, mock_make_move, mock_print, mock_input):
        """Prueba el flujo general de la partida con alternancia de turnos"""
        cli = ChessCLI()
        cli.play_game()

        # Verificar que el tablero se muestre, se realicen movimientos y se verifiquen las condiciones del juego
        mock_print.assert_any_call("Bienvenido al juego de ajedrez.")
        mock_input.assert_any_call("¿Desean terminar el juego? (s/n): ")  # Verifica que se pregunta si se quiere finalizar

        # Verificación de los movimientos de ambos jugadores
        mock_make_move.assert_any_call((6, 4), (4, 4))  # Movimiento del peón blanco de 'e2' a 'e4'
        mock_make_move.assert_any_call((1, 4), (3, 4))  # Movimiento del peón negro de 'e7' a 'e5'
        mock_make_move.assert_any_call((7, 6), (5, 5))  # Movimiento del caballo blanco de 'g1' a 'f3'

        mock_print.assert_any_call("Movimiento válido")
        
        # Verificar que check_end_conditions se llame 3 veces, una después de cada movimiento
        self.assertEqual(mock_check_end_conditions.call_count, 3)

    @patch('builtins.input', side_effect=['s'])  # Simula que el jugador quiere finalizar el juego
    @patch('builtins.print')
    @patch('game.chess.Chess.end_game_by_agreement')
    @patch('game.chess.Chess.check_end_conditions', return_value=(True, "Fin del juego por acuerdo mutuo"))
    def test_end_game_by_agreement(self, mock_check_end_conditions, mock_end_game_by_agreement, mock_print, mock_input):
        """Prueba que el juego pueda terminar por acuerdo mutuo"""
        cli = ChessCLI()
        cli.play_game()

        # Verificar que el método end_game_by_agreement sea llamado
        mock_end_game_by_agreement.assert_called_once()
        mock_print.assert_any_call("El juego ha terminado por mutuo acuerdo.")

if __name__ == '__main__':
    unittest.main()






    
