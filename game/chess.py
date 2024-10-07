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

    def make_move(self, from_pos, to_pos):
        """Realiza un movimiento en el tablero"""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.board.get_piece(from_row, from_col)

        if piece is None:
            return False, "No hay ninguna pieza en esa posición."

        if not self.is_valid_turn(piece):
            return False, f"No es el turno del jugador {piece.get_color()}."

        if piece.is_valid_piece_move(self.board, from_pos, to_pos):
            self.board.move_piece(from_row, from_col, to_row, to_col)
            self.switch_turn()
            return True, f"{piece.get_color()} {piece.symbol()} se movió de {from_pos} a {to_pos}"
        else:
            return False, "Movimiento inválido."

    def check_end_conditions(self):
        """Verifica si se cumplen las condiciones para finalizar el juego"""
        white_pieces = self.board.get_pieces("WHITE")
        black_pieces = self.board.get_pieces("BLACK")

        if len(white_pieces) == 0:
            self.is_game_over = True
            return True, "Las piezas blancas han sido eliminadas. ¡Ganan las negras!"
        elif len(black_pieces) == 0:
            self.is_game_over = True
            return True, "Las piezas negras han sido eliminadas. ¡Ganan las blancas!"
        return False, None

    def end_game_by_agreement(self):
        """Termina el juego por acuerdo mutuo de ambos jugadores"""
        self.is_game_over = True
