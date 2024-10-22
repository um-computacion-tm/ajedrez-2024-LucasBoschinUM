from game.class_pieces import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(from_row, from_col)
        possibles.extend(self.get_possible_positions_eat(from_row, from_col))
        return possibles

    def get_capture_positions(self, from_row, from_col, row_offset, col_offset, opponent_color):
        possible_positions = []
        new_row = from_row + row_offset
        new_col = from_col + col_offset
        if 0 <= new_col < 8:
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece and other_piece.__color__ == opponent_color:
                possible_positions.append((new_row, new_col))
        return possible_positions

    def get_capture_positions_for_color(self, from_row, from_col, offsets, opponent_color):
        possible_positions = []
        possible_positions.extend(self.get_capture_positions(from_row, from_col, offsets['row_offset'], offsets['col_offset1'], opponent_color))
        possible_positions.extend(self.get_capture_positions(from_row, from_col, offsets['row_offset'], offsets['col_offset2'], opponent_color))
        return possible_positions

    def get_capture_positions_with_offsets(self, from_row, from_col, offsets, opponent_color):
        return self.get_capture_positions_for_color(from_row, from_col, offsets, opponent_color)

    def get_capture_positions_generic(self, from_row, from_col, row_offset, col_offset1, col_offset2, opponent_color):
        offsets = {'row_offset': row_offset, 'col_offset1': col_offset1, 'col_offset2': col_offset2}
        return self.get_capture_positions_with_offsets(from_row, from_col, offsets, opponent_color)

    def get_black_capture_positions(self, from_row, from_col):
        return self.get_capture_positions_generic(from_row, from_col, 1, -1, 1, "WHITE")

    def get_white_capture_positions(self, from_row, from_col):
        return self.get_capture_positions_generic(from_row, from_col, -1, -1, 1, "BLACK")

    def get_possible_positions_eat(self, from_row, from_col):
        if self.__color__ == "BLACK":
            return self.get_black_capture_positions(from_row, from_col)
        else:
            return self.get_white_capture_positions(from_row, from_col)

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