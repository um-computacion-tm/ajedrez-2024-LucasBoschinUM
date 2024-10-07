from game.class_pieces import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )

    #def possible_diagonal_positions(self, from_row, from_col):
        positions = []
        # Diagonal superior derecha
        for i in range(1, 8):
            if from_row + i < 8 and from_col + i < 8:
                positions.append((from_row + i, from_col + i))
            else:
                break
        # Diagonal superior izquierda
        for i in range(1, 8):
            if from_row + i < 8 and from_col - i >= 0:
                positions.append((from_row + i, from_col - i))
            else:
                break
        # Diagonal inferior derecha
        for i in range(1, 8):
            if from_row - i >= 0 and from_col + i < 8:
                positions.append((from_row - i, from_col + i))
            else:
                break
        # Diagonal inferior izquierda
        for i in range(1, 8):
            if from_row - i >= 0 and from_col - i >= 0:
                positions.append((from_row - i, from_col - i))
            else:
                break
        return positions