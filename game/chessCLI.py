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
        self.print_column_headers()
        for row in range(8):
            self.print_row(row)
        self.print_column_headers()

    def print_column_headers(self):
        """Imprime los encabezados de las columnas (a-h)"""
        print("  a b c d e f g h")  # Encabezado de columnas

    def print_row(self, row):
        """Imprime una fila del tablero, con sus piezas"""
        print(8 - row, end=" ")  # Encabezado de fila
        for col in range(8):
            piece = self.chess_game.board.get_piece(row, col)
            self.print_piece(piece)
        print(8 - row)  # Encabezado de fila al final

    def print_piece(self, piece):
        """Imprime una pieza o un punto para una casilla vacía"""
        if piece:
            print(piece.symbol(), end=" ")
        else:
            print(".", end=" ")  # Un punto representa una casilla vacía


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
    
    def play_game(self):
     """Inicia el bucle principal del juego de ajedrez"""
     print("Bienvenido al juego de ajedrez.")
     while not self.chess_game.is_game_over:
        self.display_board()
        print(f"Turno de {self.chess_game.current_turn}")

        # Verificar si los jugadores quieren terminar el juego antes de realizar un movimiento
        if input("¿Desean terminar el juego? (s/n): ").strip().lower() == 's':
            self.chess_game.end_game_by_agreement()
            print("El juego ha terminado por mutuo acuerdo.")
            break

        # Solicitar movimiento del jugador
        from_pos, to_pos = self.get_move_input()
        
        # Realizar movimiento
        valid_move, message = self.chess_game.make_move(from_pos, to_pos)
        print(message)

        # Verificar condiciones del juego
        game_over, end_message = self.chess_game.check_end_conditions()
        if game_over:
            print(end_message)
            break

     print("El juego ha terminado.")


    def start(self):
        """Inicia el juego llamando a play_game"""
        self.play_game()

if __name__ == "__main__":
    cli = ChessCLI()  # Crea una instancia de ChessCLI
    cli.start()  # Inicia el juego