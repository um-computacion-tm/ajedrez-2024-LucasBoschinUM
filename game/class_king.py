from game.class_pieces import Piece

class King(Piece):
    white_str = "♚"
    black_str = "♔"

    def get_possible_positions(self, from_row, from_col):
        possibles = self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )
        possible_king = []
        for (possible_row, possible_col) in possibles:
            if (
                abs(from_row - possible_row) <= 1 and
                abs(from_col - possible_col) <= 1
            ):
                possible_king.append((possible_row, possible_col))
        return possible_king

    def possible_orthogonal_positions(self, from_row, from_col):
        orthogonal_positions = [
            (from_row + 1, from_col),
            (from_row - 1, from_col),
            (from_row, from_col + 1),
            (from_row, from_col - 1)
        ]
        return self.filter_valid_positions(orthogonal_positions)

    def possible_diagonal_positions(self, from_row, from_col):
        diagonal_positions = [
            (from_row + 1, from_col + 1),
            (from_row + 1, from_col - 1),
            (from_row - 1, from_col + 1),
            (from_row - 1, from_col - 1)
        ]
        return self.filter_valid_positions(diagonal_positions)

    def filter_valid_positions(self, positions):
        valid_positions = []
        for (row, col) in positions:
            if 0 <= row < 8 and 0 <= col < 8:  
                valid_positions.append((row, col))
        return valid_positions