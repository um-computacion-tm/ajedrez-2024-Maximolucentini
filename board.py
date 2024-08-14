from pawn import Pawn
from rook import Rook
from knight import Knight


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        
        for col in range(8):
            self.grid[1][col] = Pawn("BLACK", f"{col+1}", position=(1, col))
            self.grid[6][col] = Pawn("WHITE", f"{col+1}", position=(6, col))

        
        self.grid[0][0] = Rook("BLACK", position=(0, 0))
        self.grid[0][7] = Rook("BLACK", position=(0, 7))
        self.grid[7][0] = Rook("WHITE", position=(7, 0))
        self.grid[7][7] = Rook("WHITE", position=(7, 7))

        
        self.grid[0][1] = Knight("BLACK", position=(0, 1))
        self.grid[0][6] = Knight("BLACK", position=(0, 6))
        self.grid[7][1] = Knight("WHITE", position=(7, 1))
        self.grid[7][6] = Knight("WHITE", position=(7, 6))
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]    

 
