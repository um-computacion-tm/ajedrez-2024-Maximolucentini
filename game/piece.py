class Piece:
    def __init__(self, color, position=None):
        """
        Initializes a chess piece with a specific color and position.
        Attributes:
        __color__: The color of the piece, either 'WHITE' or 'BLACK'.
        __position__: The current position of the piece as a tuple (row, col).
        """
        self.__color__ = color  
        """The color of the piece"""
        self.__position__ = position  
        """The initial position of the piece"""
        
    def symbol(self):
        """
        Returns a symbol representing the piece.
        This method will be overridden in subclasses.
        Raises:
        NotImplementedError: If called from the base class.
        """
        raise NotImplementedError

    def get_color(self):
        """
        Returns the color of the piece.
        Returns:
        str: The color of the piece, either 'WHITE' or 'BLACK'.
        """
        return self.__color__
    
    def get_position(self):
        """
        Returns the current position of the piece.
        Returns:
        tuple: The current position of the piece as (row, col).
        """
        return self.__position__

    def set_position(self, position):
        """
        Sets a new position for the piece.
        Parameters:
        position (tuple): The new position as (row, col).
        """
        self.__position__ = position

    def is_valid_destination(self, board, to_pos):
        """
        Checks if the destination position is valid, ensuring it's within the board boundaries
        and not occupied by a piece of the same color.
        Parameters:
        board (Board): The current board.
        to_pos (tuple): The destination position as (row, col).
        Returns:
        bool: True if the destination is valid, False otherwise.
        """
        to_row, to_col = to_pos
        if to_row < 0 or to_row >= 8 or to_col < 0 or to_col >= 8:
            return False
        piece = board.get_piece(to_row, to_col)
        if piece and piece.get_color() == self.get_color():
            return False
        return True

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """
        Checks if the move is valid for this specific piece.
        This method will be implemented by subclasses.
        Parameters:
        board (Board): The current board.
        from_pos (tuple): The starting position as (row, col).
        to_pos (tuple): The destination position as (row, col).
        Raises:
        NotImplementedError: If called from the base class.
        """
        raise NotImplementedError("This method must be implemented by subclasses.")

    def move(self, to_row, to_col):
        """
        Updates the position of the piece to the specified row and column.
        Parameters:
        to_row (int): The destination row.
        to_col (int): The destination column.
        """
        self.set_position((to_row, to_col))

    def __str__(self):
        """
        Returns a string representation of the piece, including its color and position.
        Returns:
        str: A description of the piece with its color and position.
        """
        return f"{self.__color__} Piece at {self.__position__}"
