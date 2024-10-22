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

    def is_path_clear(self, start, end, fixed, is_vertical):
        step = 1 if end > start else -1
        for pos in range(start + step, end, step):
            if is_vertical:
                if self.board.get_piece(pos, fixed) is not None:
                    return False
            else:
                if self.board.get_piece(fixed, pos) is not None:
                    return False
        return True

    def is_vertical_path_clear(self, from_row, from_col, to_row):
        return self.is_path_clear(from_row, to_row, from_col, True)

    def is_horizontal_path_clear(self, from_row, from_col, to_col):
        return self.is_path_clear(from_col, to_col, from_row, False)

    def valid_positions(self, from_row, from_col, to_row, to_col):
        is_valid = False
        if from_col == to_col and from_row != to_row:
            is_valid = self.is_vertical_path_clear(from_row, from_col, to_row)
        elif from_row == to_row and from_col != to_col:
            is_valid = self.is_horizontal_path_clear(from_row, from_col, to_col)
        return is_valid