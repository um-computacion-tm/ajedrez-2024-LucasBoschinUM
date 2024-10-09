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
            if self.is_valid_move(new_row, new_col):
                positions.append((new_row, new_col))
        return positions

    def is_valid_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        destination_piece = self.__board__.get_piece(row, col)
        if destination_piece is not None and destination_piece.get_color() == self.get_color():
            return False
        return True