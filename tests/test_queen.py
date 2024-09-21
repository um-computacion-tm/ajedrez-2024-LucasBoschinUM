import unittest
from game.class_queen import Queen
from game.class_pieces import Piece

class MockBoard:
    def get_piece(self, row, col):
        return None

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = MockBoard()
        self.queen = Queen("WHITE", self.board)

    def test_possible_positions_from_center(self):
        from_row, from_col = 4, 4
        expected_positions = self.queen.possible_orthogonal_positions(from_row, from_col) + \
                             self.queen.possible_diagonal_positions(from_row, from_col)
        self.assertEqual(self.queen.get_possible_positions(from_row, from_col), expected_positions)

    def test_possible_positions_from_corner(self):
        from_row, from_col = 0, 0
        expected_positions = self.queen.possible_orthogonal_positions(from_row, from_col) + \
                             self.queen.possible_diagonal_positions(from_row, from_col)
        self.assertEqual(self.queen.get_possible_positions(from_row, from_col), expected_positions)

    def test_possible_positions_from_edge(self):
        from_row, from_col = 0, 4
        expected_positions = self.queen.possible_orthogonal_positions(from_row, from_col) + \
                             self.queen.possible_diagonal_positions(from_row, from_col)
        self.assertEqual(self.queen.get_possible_positions(from_row, from_col), expected_positions)

if __name__ == '__main__':
    unittest.main()