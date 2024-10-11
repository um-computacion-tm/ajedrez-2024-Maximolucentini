import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.chess import Chess

class ChessCLI:
    def __init__(self):
        """
        Initializes the Chess Command Line Interface (CLI).
        Attributes:
        __chess_game__: An instance of the Chess game.
        """
        self.__chess_game__ = Chess()  
        """Instance of the Chess class"""
            

    def display_board(self):
        """
        Prints the current state of the chess board to the console.
        """
        self.print_column_headers()
        for row in range(8):
            self.print_row(row)
        self.print_column_headers()

    def print_column_headers(self):
        """
        Prints the column headers (a-h) for the chess board.
        """
        print("  a b c d e f g h")  
        """Column headers"""

    def print_row(self, row):
        """
        Prints a row of the chess board with its pieces.
        Parameters:
        row (int): The row number to be printed (0-7).
        """
        print(8 - row, end=" ")  
        """Row header"""
        for col in range(8):
            piece = self.__chess_game__.__board__.get_piece(row, col)
            self.print_piece(piece)
        print(8 - row)  
        """Row header at the end"""

    def print_piece(self, piece):
        """
        Prints a chess piece or a dot for an empty square.
        Parameters:
        piece (ChessPiece or None): The chess piece to print, or None if the square is empty.
        """
        if piece:
            print(piece.symbol(), end=" ")
        else:
            print(".", end=" ")  
            """A dot represents an empty square"""

    def get_move_input(self):
        """
        Gets the player's move input for the game.
        Returns:
        tuple: A tuple containing two positions, (from_pos, to_pos).
        """
        while True:
            try:
                from_square = input("Enter the origin position (e.g., e2): ").strip()
                to_square = input("Enter the destination position (e.g., e4): ").strip()
                from_pos = self.convert_input_to_position(from_square)
                to_pos = self.convert_input_to_position(to_square)
                return from_pos, to_pos
            except ValueError:
                print("Invalid input. Please try again.")

    def convert_input_to_position(self, square):
        """
        Converts a square like 'e2' into a board position.
        Parameters:
        square (str): The square in algebraic notation (e.g., 'e2').
        Returns:
        tuple: The (row, col) position on the board.
        """
        columns = 'abcdefgh'
        rows = '87654321'
        col = columns.index(square[0])
        row = rows.index(square[1])
        return (row, col)

    def play_game(self):
        """
        Starts the main loop for the chess game.
        Continuously displays the board, gets input, and processes moves until the game ends.
        """
        print("Welcome to the chess game.")
        while not self.__chess_game__.__is_game_over__:
            self.display_board()
            print(f"{self.__chess_game__.__current_turn__}'s turn")

            """Check if players want to end the game before making a move"""
            if input("Do you want to end the game? (y/n): ").strip().lower() == 'y':
                self.__chess_game__.end_game_by_agreement()
                print("The game has ended by mutual agreement.")
                break

            """Get player's move"""
            from_pos, to_pos = self.get_move_input()

            """Make the move"""
            valid_move, message = self.__chess_game__.make_move(from_pos, to_pos)
            print(message)

            """Check game conditions"""
            game_over, end_message = self.__chess_game__.check_end_conditions()
            if game_over:
                print(end_message)
                break

        print("The game has ended.")

    def start(self):
        """
        Starts the game by calling play_game.
        """
        self.play_game()

if __name__ == "__main__":
    cli = ChessCLI()  
    """Creates an instance of ChessCLI"""
    cli.start()  
    """Starts the game"""