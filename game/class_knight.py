from game.class_pieces import Piece

class Knight(Piece):
    white_str = "♞"
    black_str = "♘"

    def get_possible_positions(self, from_row, from_col):
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        positions = []
        for move in moves:
            new_row = from_row + move[0]
            new_col = from_col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                positions.append((new_row, new_col))
        return positions