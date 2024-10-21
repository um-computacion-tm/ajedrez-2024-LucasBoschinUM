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

    def is_vertical_path_clear(self, from_row, from_col, to_row):
        step = 1 if to_row > from_row else -1
        for row in range(from_row + step, to_row, step):
            if self.board.get_piece(row, from_col) is not None:
                return False
        return True

    def is_horizontal_path_clear(self, from_row, from_col, to_col):
        step = 1 if to_col > from_col else -1
        for col in range(from_col + step, to_col, step):
            if self.board.get_piece(from_row, col) is not None:
                return False
        return True

    def valid_positions(self, from_row, from_col, to_row, to_col):
        is_valid = False
        if from_col == to_col and from_row != to_row:
            is_valid = self.is_vertical_path_clear(from_row, from_col, to_row)
        elif from_row == to_row and from_col != to_col:
            is_valid = self.is_horizontal_path_clear(from_row, from_col, to_col)
        return is_valid