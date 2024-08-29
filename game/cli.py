from game.board import Board

class CLI:
    def __init__(self):
        self.board = Board() # Creamos un objeto del tablero

    def print_board(self):
        print(self.board) 