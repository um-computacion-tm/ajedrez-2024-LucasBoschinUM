import unittest
from game.class_board import Board
from game.class_rook import Rook
from game.exceptions import OutOfBoard

class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
                "1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
                "2                 \n"
                "3                 \n"
                "4                 \n"
                "5                 \n"
                "6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
                "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            )
        )

    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=0,
            to_col=1,
        )

        self.assertIsInstance(
            board.get_piece(0, 1),
            Rook,
        )
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "0   ♖             \n"
                "1                 \n"
                "2                 \n"
                "3                 \n"
                "4                 \n"
                "5                 \n"
                "6                 \n"
                "7                 \n"
            )
        )

    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

    def test_place_piece(self):
        board = Board(for_test=True)
        rook = Rook(color='WHITE', board=board)
        board.place_piece(rook, 0, 0)
        self.assertIs(board.get_piece(0, 0), rook)

    def test_remove_piece(self):
        board = Board(for_test=True)
        rook = Rook(color='WHITE', board=board)
        board.place_piece(rook, 0, 0)
        board.remove_piece(0, 0)
        self.assertIsNone(board.get_piece(0, 0))

    def test_has_no_pieces(self):
        board = Board(for_test=True)
        self.assertTrue(board.has_no_pieces('WHITE'))
        rook = Rook(color='WHITE', board=board)
        board.place_piece(rook, 0, 0)
        self.assertFalse(board.has_no_pieces('WHITE'))

if __name__ == '__main__':
    unittest.main()