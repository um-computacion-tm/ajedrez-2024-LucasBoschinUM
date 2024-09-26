import unittest
from game.class_bishop import Bishop
from game.class_board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bishop_white = Bishop("WHITE", self.board)
        self.bishop_black = Bishop("BLACK", self.board)

    def test_initialization(self):
        self.assertEqual(str(self.bishop_white), "♗")
        self.assertEqual(str(self.bishop_black), "♝")

    def test_get_possible_positions(self):
        from_row, from_col = 4, 4
        expected_positions = self.bishop_white.possible_diagonal_positions(from_row, from_col)
        self.assertEqual(self.bishop_white.get_possible_positions(from_row, from_col), expected_positions)

if __name__ == '__main__':
    unittest.main()