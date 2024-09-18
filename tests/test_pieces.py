import unittest
from game.class_pieces import Piece
from game.class_board import Board

class TestPiece(unittest.TestCase):
    def test_initialization(self):
        color = "WHITE"
        board = Board()
        piece = Piece(color, board)
        self.assertEqual(piece.get_color(), color)

    def test_get_color(self):
        color = "BLACK"
        board = Board()
        piece = Piece(color, board)
        self.assertEqual(piece.get_color(), color)

    def test_possible_positions_vd(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(5, 4), (6, 4), (7, 4)]
        self.assertEqual(piece.possible_positions_vd(4, 4), expected_positions)

    def test_possible_positions_va(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertEqual(piece.possible_positions_va(4, 4), expected_positions)

    def test_possible_orthogonal_positions(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertEqual(piece.possible_orthogonal_positions(4, 4), expected_positions)

    def test_possible_positions_vd_with_blocking_piece(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        blocking_piece = Piece("BLACK", board)
        board.set_piece(4, 4, piece)
        board.set_piece(6, 4, blocking_piece)
        expected_positions = [(5, 4), (6, 4)]
        self.assertEqual(piece.possible_positions_vd(4, 4), expected_positions)

    def test_possible_positions_va_with_blocking_piece(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        blocking_piece = Piece("BLACK", board)
        board.set_piece(4, 4, piece)
        board.set_piece(2, 4, blocking_piece)
        expected_positions = [(3, 4), (2, 4)]
        self.assertEqual(piece.possible_positions_va(4, 4), expected_positions)

if __name__ == '__main__':
    unittest.main()