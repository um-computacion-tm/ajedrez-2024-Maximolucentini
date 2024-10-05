from game.board import Board
from game.pawn import Pawn
from game.king import King


class Chess:
    def __init__(self):
        """Inicializa el juego de ajedrez con un tablero y las piezas"""
        self.board = Board()  # Instancia de la clase Board
        self.current_turn = "WHITE"  # El juego comienza con el turno del blanco
        self.is_game_over = False

        # Colocar las piezas iniciales en el tablero
        self.initialize_pieces()

    def initialize_pieces(self):
        """Coloca las piezas en sus posiciones iniciales en el tablero"""
        for i in range(8):
            self.board.set_piece(6, i, Pawn("WHITE", (6, i)))  # Peones blancos
            self.board.set_piece(1, i, Pawn("BLACK", (1, i)))  # Peones negros
        self.board.set_piece(7, 4, King("WHITE", (7, 4)))
        self.board.set_piece(0, 4, King("BLACK", (0, 4)))

    def switch_turn(self):
        """Alterna el turno entre los jugadores"""
        self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"

    def is_valid_turn(self, piece):
        """Verifica si es el turno del jugador correcto"""
        return piece.get_color() == self.current_turn


