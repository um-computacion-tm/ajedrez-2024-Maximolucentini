class Movement:
    def is_valid_horizontal_move(self, board, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento es horizontal.

        Args:
            board (Board): El tablero de ajedrez.
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Returns:
            bool: True si el movimiento es horizontal, False en caso contrario.
        """
        return from_row == to_row and from_col != to_col

    def is_valid_vertical_move(self, board, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento es vertical.

        Args:
            board (Board): El tablero de ajedrez.
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Returns:
            bool: True si el movimiento es vertical, False en caso contrario.
        """
        return from_col == to_col and from_row != to_row

    def is_valid_diagonal_move(self, board, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento es diagonal.

        Args:
            board (Board): El tablero de ajedrez.
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Returns:
            bool: True si el movimiento es diagonal, False en caso contrario.
        """
        return abs(from_row - to_row) == abs(from_col - to_col)

    def is_valid_lateral_move(self, board, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento es lateral (es decir, un movimiento en forma de L).

        Args:
            board (Board): El tablero de ajedrez.
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Returns:
            bool: True si el movimiento es lateral, False en caso contrario.
        """
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)

    def is_valid_jump_move(self, board, from_row, from_col, to_row, to_col):
        """
        Verifica si el movimiento es un salto (es decir, un movimiento que salta sobre otra pieza).

        Args:
            board (Board): El tablero de ajedrez.
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
            to_row (int): La fila de destino.
            to_col (int): La columna de destino.

        Returns:
            bool: True si el movimiento es un salto, False en caso contrario.
        """
        # Verificar si el movimiento es diagonal
        if not self.is_valid_diagonal_move(board, from_row, from_col, to_row, to_col):
            return False

        # Verificar si hay una pieza en el camino
        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2
        if board.get_piece(mid_row, mid_col) is None:
            return False

        # Verificar si la pieza en el camino es del oponente
        if board.get_piece(mid_row, mid_col).get_color() == self.get_color():
            return False

        return True