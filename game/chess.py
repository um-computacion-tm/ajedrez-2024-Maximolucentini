from game.board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # Validar las coordenadas
        piece = self.__board__.get_piece(from_row, from_col)