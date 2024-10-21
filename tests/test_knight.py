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

    def test_is_valid_move_within_bounds(self):
        self.assertTrue(self.knight.is_valid_move(4, 4))
        self.assertTrue(self.knight.is_valid_move(0, 0))
        self.assertTrue(self.knight.is_valid_move(7, 7))

    def test_is_valid_move_out_of_bounds(self):
        self.assertFalse(self.knight.is_valid_move(-1, 0))
        self.assertFalse(self.knight.is_valid_move(0, -1))
        self.assertFalse(self.knight.is_valid_move(8, 0))
        self.assertFalse(self.knight.is_valid_move(0, 8))

    def test_is_valid_move_occupied_by_same_color(self):
        self.board.place_piece(self.knight, 4, 4)
        self.assertFalse(self.knight.is_valid_move(4, 4))

    def test_is_valid_move_occupied_by_opponent(self):
        opponent_knight = Knight(color='BLACK', board=self.board)
        self.board.place_piece(opponent_knight, 4, 4)
        self.assertTrue(self.knight.is_valid_move(4, 4))

if __name__ == '__main__':
    unittest.main()