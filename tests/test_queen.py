import unittest
from game.class_queen import Queen
from game.class_board import Board

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.queen = Queen("WHITE", self.board)
        self.board.place_piece(self.queen, 4, 4)

    def test_possible_positions_from_center(self):
        from_row, from_col = 4, 4
        expected_positions = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimiento hacia arriba
            (5, 4), (6, 4), (7, 4),          # Movimiento hacia abajo
            (4, 5), (4, 6), (4, 7),          # Movimiento hacia la derecha
            (4, 3), (4, 2), (4, 1), (4, 0)   # Movimiento hacia la izquierda
        ]
        self.assertEqual(self.queen.possible_orthogonal_positions(from_row, from_col), expected_positions)

    def test_possible_positions_from_corner(self):
        from_row, from_col = 0, 0
        expected_positions = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Movimiento hacia abajo
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Movimiento hacia la derecha
        ]
        self.assertEqual(self.queen.possible_orthogonal_positions(from_row, from_col), expected_positions)

    def test_possible_positions_from_edge(self):
        from_row, from_col = 0, 4
        expected_positions = [
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),  # Movimiento hacia abajo
            (0, 5), (0, 6), (0, 7),                                  # Movimiento hacia la derecha
            (0, 3), (0, 2), (0, 1), (0, 0)                           # Movimiento hacia la izquierda
        ]
        self.assertEqual(self.queen.possible_orthogonal_positions(from_row, from_col), expected_positions)

    def test_get_possible_positions_from_center(self):
        from_row, from_col = 4, 4
        expected_positions = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimiento hacia arriba
            (5, 4), (6, 4), (7, 4),          # Movimiento hacia abajo
            (4, 5), (4, 6), (4, 7),          # Movimiento hacia la derecha
            (4, 3), (4, 2), (4, 1), (4, 0),  # Movimiento hacia la izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal hacia arriba a la derecha
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal hacia arriba a la izquierda
            (5, 5), (6, 6), (7, 7),          # Diagonal hacia abajo a la derecha
            (5, 3), (6, 2), (7, 1)           # Diagonal hacia abajo a la izquierda
        ]
        self.assertEqual(self.queen.get_possible_positions(from_row, from_col), expected_positions)

    def test_possible_diagonal_positions_from_center(self):
        from_row, from_col = 4, 4
        expected_positions = [
            (3, 5), (2, 6), (1, 7),          # Diagonal hacia arriba a la derecha
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal hacia arriba a la izquierda
            (5, 5), (6, 6), (7, 7),          # Diagonal hacia abajo a la derecha
            (5, 3), (6, 2), (7, 1)           # Diagonal hacia abajo a la izquierda
        ]
        self.assertEqual(self.queen.possible_diagonal_positions(from_row, from_col), expected_positions)

    def test_possible_diagonal_positions_from_corner(self):
        from_row, from_col = 0, 0
        expected_positions = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal hacia abajo a la derecha
        ]
        self.assertEqual(self.queen.possible_diagonal_positions(from_row, from_col), expected_positions)

    def test_is_valid_move(self):
        self.board.place_piece(self.queen, 4, 4)
        # Movimiento ortogonal válido
        self.assertTrue(self.queen.is_valid_move(4, 4, 4, 7))
        # Movimiento diagonal válido
        self.assertTrue(self.queen.is_valid_move(4, 4, 7, 7))
        # Movimiento ortogonal inválido (pieza en el camino)
        self.board.place_piece(Queen("WHITE", self.board), 4, 6)
        self.assertFalse(self.queen.is_valid_move(4, 4, 4, 7))
        # Movimiento diagonal inválido (pieza en el camino)
        self.board.place_piece(Queen("WHITE", self.board), 6, 6)
        self.assertFalse(self.queen.is_valid_move(4, 4, 7, 7))
        # Movimiento ortogonal válido (misma fila)
        self.assertTrue(self.queen.is_valid_move(4, 4, 4, 5))
        # Movimiento ortogonal válido (misma columna)
        self.assertTrue(self.queen.is_valid_move(4, 4, 5, 4))
        # Movimiento ortogonal inválido (fuera del tablero)
        self.assertFalse(self.queen.is_valid_move(4, 4, 4, 8))
        # Movimiento diagonal inválido (fuera del tablero)
        self.assertFalse(self.queen.is_valid_move(4, 4, 8, 8))
        # Movimiento inválido (pieza de mismo color en destino)
        self.board.place_piece(Queen("WHITE", self.board), 5, 5)
        self.assertFalse(self.queen.is_valid_move(4, 4, 5, 5))
        self.board.place_piece(Queen("WHITE", self.board), 4, 5)
        self.assertFalse(self.queen.is_valid_move(4, 4, 4, 5))

    def test_is_valid_move_vertical_blocked(self):
        self.board.place_piece(self.queen, 4, 4)
        # Colocar una pieza en el camino vertical
        self.board.place_piece(Queen("WHITE", self.board), 6, 4)
        # Movimiento ortogonal inválido (pieza en el camino)
        self.assertFalse(self.queen.is_valid_move(4, 4, 7, 4))

    def test_get_valid_moves(self):
        self.board.place_piece(self.queen, 4, 4)
        expected_moves = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimiento hacia arriba
            (5, 4), (6, 4), (7, 4),          # Movimiento hacia abajo
            (4, 5), (4, 6), (4, 7),          # Movimiento hacia la derecha
            (4, 3), (4, 2), (4, 1), (4, 0),  # Movimiento hacia la izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal hacia arriba a la derecha
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal hacia arriba a la izquierda
            (5, 5), (6, 6), (7, 7),          # Diagonal hacia abajo a la derecha
            (5, 3), (6, 2), (7, 1)           # Diagonal hacia abajo a la izquierda
        ]
        self.assertEqual(self.queen.get_valid_moves(4, 4), expected_moves)

    def test_invalid_move(self):
        self.board.place_piece(self.queen, 4, 4)
        # Movimiento inválido (no ortogonal ni diagonal)
        self.assertFalse(self.queen.is_valid_move(4, 4, 5, 6))

if __name__ == '__main__':
    unittest.main()