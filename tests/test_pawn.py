import unittest
from game.class_pawn import Pawn
from game.class_board import Board

class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board(for_test=True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        board = Board(for_test=True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_eat_left_black(self):
        board = Board(for_test=True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 4, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 4)]
        )

    def test_eat_right_black(self):
        board = Board(for_test=True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 6)]
        )

    def test_initial_white(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4)]
        )

    def test_not_initial_white_block(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_not_initial_black_block(self):
        board = Board(for_test=True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 5, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            []
        )

    def test_eat_left_white(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 3, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4), (4, 3)]
        )

    def test_eat_right_white(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 5, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4), (4, 5)]
        )

    def test_initial_white_double_move(self):
        board = Board(for_test=True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

if __name__ == '__main__':
    unittest.main()