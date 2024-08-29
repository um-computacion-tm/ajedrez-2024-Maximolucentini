import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from game.piece import *
from game.board import *
from game.pawn import *

class TestPawn(unittest.TestCase):
    def test_initial_move():
     board = Board()  
     """Asume un tablero vacio"""
     pawn = Pawn("WHITE", (6, 0)) 
     """Peón blanco en fila 6, columna 0"""
     assert pawn.is_valid_move(board, 6, 0, 4, 0)
     """Mueve dos pasos hacia adelante"""
     
    def test_normal_move():
     board = Board()  
     """Asume un tablero vacio"""
     pawn = Pawn("BLACK", (1, 0))  
     """peón negro en fila 1, columna 0"""
     assert pawn.is_valid_move(board, 1, 0, 2, 0) 
     """mueve un paso hacia adelante"""
     
    def test_capture():
     board = Board()               
     """Asume un tablero vacio"""
     pawn = Pawn("WHITE", (3, 3))  
     """Peón blanco en fila 3, columna 3"""
     opponent_pawn = Pawn("BLACK", (4, 4))  
     """Peón negro en fila 4, columna 4"""
     board.set_piece(4, 4, opponent_pawn)  
     """Establece el peón oponente en el tablero"""
     assert pawn.is_valid_move(board, 3, 3, 4, 4)  
     """Captura diagonal hacia adelante"""
     
    def test_invalid_move_backwards():
     board = Board()  
     """Asume un tablero vacio"""
     pawn = Pawn("BLACK", (2, 0))  # black pawn at row 2, col 0
     """Peón blanco en fila 2, columna 0"""
     assert not pawn.is_valid_move(board, 2, 0, 1, 0)
     """Intenta mover hacia atrás"""
     
    def test_invalid_move_sideways():
     board = Board()  
     """Asume un tablero vacio"""
     pawn = Pawn("WHITE", (5, 0))  
     """Peón blanco en fila 5, columna 0"""
     assert not pawn.is_valid_move(board, 5, 0, 5, 1) 
     """Intenta mover hacia los lados"""
     
    def test_move_and_update_position():
     board = Board()  
     """Asume un tablero vacio"""
     pawn = Pawn("BLACK", (1, 0))  
     """Peón negro en fila 1, columna 0"""
     pawn.move(board, 2, 0) 
     """Mueve un paso hacia adelante"""
     assert pawn.__position__ == (2, 0) 
     """Posición debe ser actualizada"""
     
    
if __name__ == '__main__':    
    unittest.main()
