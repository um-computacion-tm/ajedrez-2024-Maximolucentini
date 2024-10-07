import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from game.chess import Chess

class ChessCLI:
    def __init__(self):
        """Inicializa la interfaz de línea de comando del juego de ajedrez"""
        self.chess_game = Chess()  # Instancia de la clase Chess

    def display_board(self):
        """Imprime el tablero en la consola"""
        print("  a b c d e f g h")  # Encabezado de columnas
        for row in range(8):
            print(8 - row, end=" ")  # Encabezado de filas
            for col in range(8):
                piece = self.chess_game.board.get_piece(row, col)
                if piece:
                    print(piece.symbol(), end=" ")
                else:
                    print(".", end=" ")  # Un punto representa una casilla vacía
            print(8 - row)  # Encabezado de fila al final
        print("  a b c d e f g h")  # Encabezado de columnas al final

    def get_move_input(self):
        """Obtiene la entrada del movimiento del usuario"""
        while True:
            try:
                from_square = input("Ingrese la posición de origen (ej: e2): ").strip()
                to_square = input("Ingrese la posición de destino (ej: e4): ").strip()
                from_pos = self.convert_input_to_position(from_square)
                to_pos = self.convert_input_to_position(to_square)
                return from_pos, to_pos
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")

    def convert_input_to_position(self, square):
        """Convierte una entrada como 'e2' a una posición en el tablero"""
        columns = 'abcdefgh'
        rows = '87654321'
        col = columns.index(square[0])
        row = rows.index(square[1])
        return (row, col)
