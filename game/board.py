from game.rook import Rook
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn

class Board:
    def __init__(self):
        """
        Initializes the board with an 8x8 grid and places the pieces in their initial positions.
        Attributes:
        __positions__: A 2D list representing the board and holding chess pieces or None for empty squares.
        """
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__setup_board__()

    def __setup_board__(self):
        """
        Sets up the initial positions of the pieces on the board.
        """
        """Set up pawns"""
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")

        """Set up rooks"""
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        """Set up knights"""
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        """Set up bishops"""
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        """Set up queens"""
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        """Set up kings"""
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    def get_piece(self, row, col):
        """
        Gets the piece at a specific position on the board.
        Parameters:
        row (int): The row index (0-7).
        col (int): The column index (0-7).
        Returns:
        ChessPiece or None: The piece at the specified position or None if the square is empty.
        """
        return self.__positions__[row][col]
    
    def get_pieces_in_row(self, row, color):
        """
        Returns all pieces of a specific color in a given row.
        Parameters:
        row (int): The row index (0-7).
        color (str): The color of the pieces ('WHITE' or 'BLACK').
        Returns:
        list: A list of pieces of the specified color in the row.
        """
        pieces = []
        for col in range(8):
            piece = self.get_piece(row, col)
            if piece is not None and piece.get_color() == color:
                pieces.append(piece)
        return pieces

    def get_pieces(self, color):
        """
        Returns all pieces of a specific color on the board.
        Parameters:
        color (str): The color of the pieces ('WHITE' or 'BLACK').
        Returns:
        list: A list of all pieces of the specified color on the board.
        """
        pieces = []
        for row in range(8):
            pieces.extend(self.get_pieces_in_row(row, color))
        return pieces
    
    def set_piece(self, row, col, piece):
        """
        Sets a piece at a specific position on the board.
        Parameters:
        row (int): The row index (0-7).
        col (int): The column index (0-7).
        piece (ChessPiece or None): The piece to place at the specified position or None to empty the square.
        """
        self.__positions__[row][col] = piece

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        """
        Checks if a move is valid by verifying the piece's movement rules and destination.
        Parameters:
        from_row (int): The starting row index.
        from_col (int): The starting column index.
        to_row (int): The destination row index.
        to_col (int): The destination column index.
        Returns:
        bool: True if the move is valid, False otherwise.
        """
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False
        return piece.is_valid_piece_move(self, (from_row, from_col), (to_row, to_col)) and \
               piece.is_valid_destination(self, (to_row, to_col))  

    def move_piece(self, from_row, from_col, to_row, to_col):
        """
        Moves a piece from one position to another, validating the move.
        Parameters:
        from_row (int): The starting row index.
        from_col (int): The starting column index.
        to_row (int): The destination row index.
        to_col (int): The destination column index.
        Raises:
        ValueError: If there is no piece at the starting position, if the destination is occupied by a friendly piece,
                    or if the move is invalid.
        """
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No piece at the starting position.")

        dest_piece = self.get_piece(to_row, to_col)
        if dest_piece and dest_piece.get_color() == piece.get_color():
            raise ValueError("The destination is already occupied by a piece of the same color.")

        if not piece.is_valid_piece_move(self, (from_row, from_col), (to_row, to_col)):
            raise ValueError("Invalid move.")

        """Valid move, update the positions"""
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

        """If the piece is a pawn, update its initial position status"""
        if isinstance(piece, Pawn):
            piece.__initial_position__ = False

    def show_board(self):
        """
        Returns a textual representation of the board.
        Returns:
        str: A string showing the current state of the board with pieces and empty squares.
        """
        return "\n".join(" ".join(piece.symbol() if piece else "." for piece in row) for row in self.__positions__)


 