from game.class_pieces import Piece

class Pawn(Piece):
    white_str = "♜"
    black_str = "♖"

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(
            from_row,
            from_col,
        )
        possibles.extend(
            self.get_possible_positions_eat(from_row, from_col)
        )
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        if self.__color__ == "BLACK":
            other_piece = self.__board__.get_piece(from_row + 1, from_col + 1)
            if other_piece and other_piece.__color__ == "WHITE":
                return [(from_row + 1, from_col + 1)]

        return []

    def get_possible_positions_move(self, from_row, from_col):
        possible_positions = []

        if self.__color__ == "BLACK":
            if self.__board__.get_piece(from_row + 1, from_col) is None:
                possible_positions.append((from_row + 1, from_col))
                if from_row == 1 and self.__board__.get_piece(from_row + 2, from_col) is None:
                    possible_positions.append((from_row + 2, from_col))
        else:
            if from_row == 6:
                possible_positions.extend([(from_row - 1, from_col), (from_row - 2, from_col)])
            elif self.__board__.get_piece(from_row - 1, from_col) is None:
                possible_positions.append((from_row - 1, from_col))

        return possible_positions