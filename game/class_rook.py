from game.class_pieces import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def __init__(self, color, board):
        self.color = color
        self.board = board

    def get_color(self):
        return self.color

    def __str__(self):
        return "♜" if self.color == "WHITE" else "♖"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimiento vertical
        if from_col == to_col and from_row != to_row:
            # Verificar que no haya piezas en el camino
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.board.get_piece(row, from_col) is not None:
                    return False
            return True
        # Movimiento horizontal
        if from_row == to_row and from_col != to_col:
            # Verificar que no haya piezas en el camino
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.board.get_piece(from_row, col) is not None:
                    return False
            return True
        return False

    def possible_positions_vd(self, from_row, from_col):
        positions = []
        for row in range(from_row + 1, 8):
            piece = self.board.get_piece(row, from_col)
            if piece is None:
                positions.append((row, from_col))
            else:
                if piece.get_color() != self.color:
                    positions.append((row, from_col))
                break
        return positions

    def possible_positions_va(self, from_row, from_col):
        positions = []
        for row in range(from_row - 1, -1, -1):
            piece = self.board.get_piece(row, from_col)
            if piece is None:
                positions.append((row, from_col))
            else:
                if piece.get_color() != self.color:
                    positions.append((row, from_col))
                break
        return positions

    def possible_positions_hd(self, from_row, from_col):
        positions = []
        for col in range(from_col + 1, 8):
            piece = self.board.get_piece(from_row, col)
            if piece is None:
                positions.append((from_row, col))
            else:
                if piece.get_color() != self.color:
                    positions.append((from_row, col))
                break
        return positions

    def possible_positions_ha(self, from_row, from_col):
        positions = []
        for col in range(from_col - 1, -1, -1):
            piece = self.board.get_piece(from_row, col)
            if piece is None:
                positions.append((from_row, col))
            else:
                if piece.get_color() != self.color:
                    positions.append((from_row, col))
                break
        return positions