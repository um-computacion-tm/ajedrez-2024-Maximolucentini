from game.board import Board
from game.pawn import Pawn
from game.king import King


class Chess:
    def __init__(self):
        """
        Initializes the chess game with a board and pieces.
        Attributes:
        __board__: The chess board.
        __current_turn__: The current player's turn ('WHITE' or 'BLACK').
        __is_game_over__: Boolean indicating if the game has ended.
        """
        self.__board__ = Board()  
        """Instance of the Board class"""
        self.__current_turn__ = "WHITE"  
        """The game starts with White's turn"""
        self.__is_game_over__ = False

        """Place the initial pieces on the board"""
        self.__initialize_pieces__()

    def __initialize_pieces__(self):
        """
        Sets up the pieces on their initial positions on the board.
        """
        for i in range(8):
            self.__board__.set_piece(6, i, Pawn("WHITE", (6, i)))  
            self.__board__.set_piece(1, i, Pawn("BLACK", (1, i)))
        self.__board__.set_piece(7, 4, King("WHITE", (7, 4)))
        self.__board__.set_piece(0, 4, King("BLACK", (0, 4)))

    def __switch_turn__(self):
        """
        Alternates the turn between players.
        """
        self.__current_turn__ = "BLACK" if self.__current_turn__ == "WHITE" else "WHITE"

    def __is_valid_turn__(self, piece):
        """
        Checks if it is the correct player's turn to move the given piece.
        Parameters:
        piece (ChessPiece): The piece to check.
        Returns:
        bool: True if it's the correct turn, False otherwise.
        """
        return piece.get_color() == self.__current_turn__

    def make_move(self, from_pos, to_pos):
        """
        Makes a move on the board.
        Parameters:
        from_pos (tuple): The starting position of the piece.
        to_pos (tuple): The ending position of the piece.
        Returns:
        tuple: A boolean indicating if the move is valid and a message describing the result.
        """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.__board__.get_piece(from_row, from_col)

        if piece is None:
            return False, "No piece at the selected position."

        if not self.__is_valid_turn__(piece):
            return False, f"It's not {piece.get_color()}'s turn."

        if piece.is_valid_piece_move(self.__board__, from_pos, to_pos):
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            self.__switch_turn__()
            return True, f"{piece.get_color()} {piece.symbol()} moved from {from_pos} to {to_pos}"
        else:
            return False, "Invalid move."

    def check_end_conditions(self):
        """
        Checks if the game has met the end conditions.
        Returns:
        tuple: A boolean indicating if the game is over and a message, or None if the game is not over.
        """
        white_pieces = self.__board__.get_pieces("WHITE")
        black_pieces = self.__board__.get_pieces("BLACK")

        if len(white_pieces) == 0:
            self.__is_game_over__ = True
            return True, "White pieces have been eliminated. Black wins!"
        elif len(black_pieces) == 0:
            self.__is_game_over__ = True
            return True, "Black pieces have been eliminated. White wins!"
        return False, None

    def end_game_by_agreement(self):
        """
        Ends the game by mutual agreement of both players.
        """
        self.__is_game_over__ = True
