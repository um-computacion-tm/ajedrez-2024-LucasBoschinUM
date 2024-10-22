from game.class_pieces import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(from_row, from_col)
        possibles.extend(self.get_possible_positions_eat(from_row, from_col))
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        def add_position_if_valid(row_offset, col_offset, target_color):
            new_row, new_col = from_row + row_offset, from_col + col_offset
            if 0 <= new_col <= 7:
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece and other_piece.__color__ == target_color:
                    possible_positions.append((new_row, new_col))

        possible_positions = []
        if self.__color__ == "BLACK":
            add_position_if_valid(1, -1, "WHITE")
            add_position_if_valid(1, 1, "WHITE")
        else:
            add_position_if_valid(-1, -1, "BLACK")
            add_position_if_valid(-1, 1, "BLACK")

        return possible_positions

    def get_possible_positions_move(self, from_row, from_col):
        possible_positions = []
        if self.__color__ == "BLACK":
            if self.__board__.get_piece(from_row + 1, from_col) is None:
                possible_positions.append((from_row + 1, from_col))
                if from_row == 1 and self.__board__.get_piece(from_row + 2, from_col) is None:
                    possible_positions.append((from_row + 2, from_col))
        else:
            if self.__board__.get_piece(from_row - 1, from_col) is None:
                possible_positions.append((from_row - 1, from_col))
                if from_row == 6 and self.__board__.get_piece(from_row - 2, from_col) is None:
                    possible_positions.append((from_row - 2, from_col))
        return possible_positions