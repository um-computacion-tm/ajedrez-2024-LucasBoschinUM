import unittest
from game.class_knight import Knight
from game.class_board import Board

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.knight = Knight(color='WHITE', board=self.board)

    def test_initialization(self):
        self.assertEqual(self.knight.get_color(), 'WHITE')
        self.assertEqual(str(self.knight), '♞')

    def test_get_possible_positions(self):
        positions = self.knight.get_possible_positions(4, 4)
        expected_positions = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        self.assertCountEqual(positions, expected_positions)

if __name__ == '__main__':
    unittest.main()