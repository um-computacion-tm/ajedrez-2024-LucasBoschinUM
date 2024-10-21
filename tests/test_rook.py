import unittest
from game.class_rook import Rook
from game.class_board import Board
from game.class_pawn import Pawn

class TestRook(unittest.TestCase):
    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_diagonal_desc(self):
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )

        self.assertFalse(is_possible)

    def test_move_horizontal_right(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_hd(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_left(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_ha(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_valid_positions_vertical(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        self.assertTrue(rook.valid_positions(4, 1, 7, 1))
        self.assertFalse(rook.valid_positions(4, 1, 4, 1))

    def test_valid_positions_horizontal(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        self.assertTrue(rook.valid_positions(4, 1, 4, 7))
        self.assertFalse(rook.valid_positions(4, 1, 4, 1))

    def test_valid_positions_invalid(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        self.assertFalse(rook.valid_positions(4, 1, 5, 2))

    def test_possible_positions_vd_with_own_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(6, 1, pawn)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_possible_positions_va_with_own_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(2, 1, pawn)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1)]
        )

    def test_possible_positions_hd_with_own_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(4, 3, pawn)
        possibles = rook.possible_positions_hd(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2)]
        )

    def test_possible_positions_ha_with_own_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, rook)
        board.set_piece(4, 2, pawn)
        possibles = rook.possible_positions_ha(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_valid_positions_with_piece_in_way(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(5, 1, pawn)
        self.assertFalse(rook.valid_positions(4, 1, 6, 1))

    def test_possible_positions_va_with_piece_in_way(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(2, 1, pawn)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1)]
        )

    def test_possible_positions_hd_with_piece_in_way(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 1, rook)
        board.set_piece(4, 3, pawn)
        possibles = rook.possible_positions_hd(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2)]
        )

    def test_possible_positions_ha_with_piece_in_way(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, rook)
        board.set_piece(4, 2, pawn)
        possibles = rook.possible_positions_ha(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_possible_positions_vd_with_enemy_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("BLACK", board)
        board.set_piece(4, 1, rook)
        board.set_piece(6, 1, pawn)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_possible_positions_va_with_enemy_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("BLACK", board)
        board.set_piece(4, 1, rook)
        board.set_piece(2, 1, pawn)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1)]
        )

    def test_possible_positions_hd_with_enemy_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("BLACK", board)
        board.set_piece(4, 1, rook)
        board.set_piece(4, 3, pawn)
        possibles = rook.possible_positions_hd(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3)]
        )

    def test_possible_positions_ha_with_enemy_piece(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)
        pawn = Pawn("BLACK", board)
        board.set_piece(4, 4, rook)
        board.set_piece(4, 2, pawn)
        possibles = rook.possible_positions_ha(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2)]
        )

if __name__ == '__main__':
    unittest.main()