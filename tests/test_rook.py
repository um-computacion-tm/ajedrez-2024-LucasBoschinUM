import unittest
from game.class_board import Board
from game.class_rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.rook = Rook("WHITE", self.board)
        self.board.place_piece(self.rook, 4, 4)

    def test_is_vertical_path_clear(self):
        # Path clear
        self.assertTrue(self.rook.is_vertical_path_clear(4, 4, 7))
        # Path blocked
        self.board.place_piece(Rook("WHITE", self.board), 6, 4)
        self.assertFalse(self.rook.is_vertical_path_clear(4, 4, 7))

    def test_is_horizontal_path_clear(self):
        # Path clear
        self.assertTrue(self.rook.is_horizontal_path_clear(4, 4, 7))
        # Path blocked
        self.board.place_piece(Rook("WHITE", self.board), 4, 6)
        self.assertFalse(self.rook.is_horizontal_path_clear(4, 4, 7))

    def test_valid_positions(self):
        # Valid vertical move
        self.assertTrue(self.rook.valid_positions(4, 4, 7, 4))
        # Valid horizontal move
        self.assertTrue(self.rook.valid_positions(4, 4, 4, 7))
        # Invalid move (not vertical or horizontal)
        self.assertFalse(self.rook.valid_positions(4, 4, 5, 5))

    def test_invalid_move(self):
        # Invalid move (not vertical or horizontal)
        self.assertFalse(self.rook.valid_positions(4, 4, 5, 5))

if __name__ == '__main__':
    unittest.main()