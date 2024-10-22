class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def get_color(self):
        return self.__color__

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_diagonal_positions(self, from_row, from_col):
        return []

    def _get_positions(self, from_row, from_col, position_functions):
        possibles = []
        self.extend_positions(possibles, position_functions)
        return possibles

    def possible_orthogonal_positions(self, from_row, from_col):
        return self._get_positions(from_row, from_col, [
            lambda: self.possible_positions_vd(from_row, from_col),
            lambda: self.possible_positions_va(from_row, from_col)
        ])

    def possible_positions(self, row, col, row_increment, limit_condition):
        possibles = []
        next_row = row + row_increment
        while limit_condition(next_row):
            other_piece = self.__board__.get_piece(next_row, col)
            if (other_piece is not None):
                if (other_piece.get_color() != self.get_color()):
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
            next_row += row_increment
        return possibles

    def possible_positions_vd(self, row, col):
        return self.possible_positions(row, col, 1, lambda r: r < 8)

    def possible_positions_va(self, row, col):
        return self.possible_positions(row, col, -1, lambda r: r >= 0)

    def get_combined_positions(self, from_row, from_col):
        return self._get_positions(from_row, from_col, [
            lambda: self.possible_diagonal_positions(from_row, from_col),
            lambda: self.possible_orthogonal_positions(from_row, from_col)
        ])

    def get_possible_positions(self, from_row, from_col):
        return self.get_combined_positions(from_row, from_col)

    def extend_positions(self, positions, position_functions):
        for func in position_functions:
            positions.extend(func())