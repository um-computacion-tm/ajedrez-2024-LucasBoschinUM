from game.class_pieces import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )

    def possible_diagonal_positions(self, from_row, from_col):
        possibles = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for row_inc, col_inc in directions:
            next_row, next_col = from_row + row_inc, from_col + col_inc
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                piece = self.__board__.get_piece(next_row, next_col)
                if piece is None:
                    possibles.append((next_row, next_col))
                elif piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
                    break
                else:
                    break
                next_row += row_inc
                next_col += col_inc
        
        return possibles