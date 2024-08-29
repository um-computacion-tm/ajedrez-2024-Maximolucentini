from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", position=(1, col))
            self.__positions__[6][col] = Pawn("WHITE", position=(6, col))


        
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    def get_piece(self, row, col):
        
        return self.__positions__[row][col]
    
    def move_piece(self, from_row, from_col, to_row, to_col):
     piece = self.get_piece(from_row, from_col)
     if piece is None:
        raise ValueError("No hay pieza en la posición de origen")
     dest_piece = self.get_piece(to_row, to_col)
     if dest_piece is not None and dest_piece.__class__ == piece.__class__:
        raise ValueError("La posición de destino ya está ocupada por una pieza del mismo tipo")
     if piece.is_valid_move(self, from_row, from_col, to_row, to_col):
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None
     else:
        raise ValueError("Movimiento inválido")
    def show_board(self):
        """Devuelve una representación textual del tablero"""
        board_str = ""
        for row in self.__positions__:
            for piece in row:
                if piece is None:
                    board_str += ". "
                else:
                    board_str += piece.symbol + " "
            board_str += "\n"
        return board_str       
   

 