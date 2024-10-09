import unittest
from game.class_king import King
from game.class_board import Board

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.king = King("WHITE", self.board)

    def test_possible_positions_center(self):
        from_row, from_col = 4, 4
        expected_positions = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        self.assertCountEqual(self.king.get_possible_positions(from_row, from_col), expected_positions)

    def test_possible_positions_corner(self):
        from_row, from_col = 0, 0
        expected_positions = [
            (0, 1),
            (1, 0), (1, 1)
        ]
        self.assertCountEqual(self.king.get_possible_positions(from_row, from_col), expected_positions)

    def test_possible_positions_edge(self):
        from_row, from_col = 0, 4
        expected_positions = [
            (0, 3), (0, 5),
            (1, 3), (1, 4), (1, 5)
        ]
        self.assertCountEqual(self.king.get_possible_positions(from_row, from_col), expected_positions)

if __name__ == '__main__':
    unittest.main()