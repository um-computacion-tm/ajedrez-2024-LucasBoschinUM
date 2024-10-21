from game.class_pieces import Piece

class Queen(Piece):
    white_str = "♛"
    black_str = "♕"

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )

    def possible_diagonal_positions(self, from_row, from_col):
        possibles = []
        # Diagonal hacia arriba a la derecha
        for i in range(1, 8):
            if from_row - i < 0 or from_col + i > 7:
                break
            possibles.append((from_row - i, from_col + i))
        # Diagonal hacia arriba a la izquierda
        for i in range(1, 8):
            if from_row - i < 0 or from_col - i < 0:
                break
            possibles.append((from_row - i, from_col - i))
        # Diagonal hacia abajo a la derecha
        for i in range(1, 8):
            if from_row + i > 7 or from_col + i > 7:
                break
            possibles.append((from_row + i, from_col + i))
        # Diagonal hacia abajo a la izquierda
        for i in range(1, 8):
            if from_row + i > 7 or from_col - i < 0:
                break
            possibles.append((from_row + i, from_col - i))
        return possibles

    def possible_orthogonal_positions(self, from_row, from_col):
        possibles = []
        # Movimiento hacia arriba
        for i in range(1, 8):
            if from_row - i < 0:
                break
            possibles.append((from_row - i, from_col))
        # Movimiento hacia abajo
        for i in range(1, 8):
            if from_row + i > 7:
                break
            possibles.append((from_row + i, from_col))
        # Movimiento hacia la derecha
        for i in range(1, 8):
            if from_col + i > 7:
                break
            possibles.append((from_row, from_col + i))
        # Movimiento hacia la izquierda
        for i in range(1, 8):
            if from_col - i < 0:
                break
            possibles.append((from_row, from_col - i))
        return possibles

    def is_within_board_limits(self, to_row, to_col):
        return 0 <= to_row < 8 and 0 <= to_col < 8

    def is_destination_occupied_by_same_color(self, to_row, to_col):
        destination_piece = self.__board__.get_piece(to_row, to_col)
        return destination_piece and destination_piece.get_color() == self.get_color()

    def is_path_clear_orthogonal(self, from_row, from_col, to_row, to_col):
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if self.__board__.get_piece(from_row, col):
                    return False
        elif from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if self.__board__.get_piece(row, from_col):
                    return False
        return True

    def is_path_clear_diagonal(self, from_row, from_col, to_row, to_col):
        path_clear = True
        if abs(from_row - to_row) == abs(from_col - to_col):
            row_step = 1 if to_row > from_row else -1
            col_step = 1 if to_col > from_col else -1
            for i in range(1, abs(from_row - to_row)):
                if self.__board__.get_piece(from_row + i * row_step, from_col + i * col_step):
                    path_clear = False
                    break
        return path_clear

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        is_valid = True
        
        if not self.is_within_board_limits(to_row, to_col):
            is_valid = False
        elif self.is_destination_occupied_by_same_color(to_row, to_col):
            is_valid = False
        elif from_row == to_row or from_col == to_col:
            if not self.is_path_clear_orthogonal(from_row, from_col, to_row, to_col):
                is_valid = False
        elif abs(from_row - to_row) == abs(from_col - to_col):
            if not self.is_path_clear_diagonal(from_row, from_col, to_row, to_col):
                is_valid = False
        else:
            is_valid = False
        
        return is_valid

    def get_valid_moves(self, from_row, from_col):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return [(to_row, to_col) for to_row, to_col in possible_positions if self.is_valid_move(from_row, from_col, to_row, to_col)]