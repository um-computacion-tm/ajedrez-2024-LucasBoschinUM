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