import unittest
from game.class_chess import Chess
from game.class_board import Board
from game.class_rook import Rook
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.chess._Chess__board__ = Board(for_test=True)  # Inicializar el tablero correctamente

    def test_initial_turn(self):
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

    def test_move_changes_turn(self):
        self.chess._Chess__board__.set_piece(7, 0, Rook("WHITE", self.chess._Chess__board__))
        self.chess.move(7, 0, 6, 0)
        self.assertEqual(self.chess.turn, "BLACK")

    def test_invalid_move_out_of_board(self):
        with self.assertRaises(OutOfBoard):
            self.chess.move(0, 0, 8, 8)

    def test_invalid_move_empty_position(self):
        with self.assertRaises(EmptyPosition):
            self.chess.move(4, 4, 5, 5)

    def test_invalid_move_opponent_piece(self):
        self.chess._Chess__board__.set_piece(0, 0, Rook("BLACK", self.chess._Chess__board__))
        with self.assertRaises(InvalidTurn):
            self.chess.move(0, 0, 1, 0)

    def test_invalid_move(self):
        self.chess._Chess__board__.set_piece(7, 0, Rook("WHITE", self.chess._Chess__board__))
        with self.assertRaises(InvalidMove):
            self.chess.move(7, 0, 7, 7)

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())

    def test_end_game_white_wins(self):
        self.chess._Chess__board__.remove_piece(0, 0)  # Remover todas las piezas negras
        self.chess._Chess__board__.remove_piece(0, 7)
        self.chess._Chess__board__.remove_piece(0, 1)
        self.chess._Chess__board__.remove_piece(0, 6)
        self.chess._Chess__board__.remove_piece(0, 2)
        self.chess._Chess__board__.remove_piece(0, 5)
        self.chess._Chess__board__.remove_piece(0, 3)
        self.chess._Chess__board__.remove_piece(0, 4)
        for col in range(8):
            self.chess._Chess__board__.remove_piece(1, col)
        self.chess.end_game()
        self.assertFalse(self.chess.is_playing())

    def test_end_game_black_wins(self):
        self.chess._Chess__board__.remove_piece(7, 0)  # Remover todas las piezas blancas
        self.chess._Chess__board__.remove_piece(7, 7)
        self.chess._Chess__board__.remove_piece(7, 1)
        self.chess._Chess__board__.remove_piece(7, 6)
        self.chess._Chess__board__.remove_piece(7, 2)
        self.chess._Chess__board__.remove_piece(7, 5)
        self.chess._Chess__board__.remove_piece(7, 3)
        self.chess._Chess__board__.remove_piece(7, 4)
        for col in range(8):
            self.chess._Chess__board__.remove_piece(6, col)
        self.chess.end_game()
        self.assertFalse(self.chess.is_playing())

    def test_end_by_agreement(self):
        self.chess.end_by_agreement()
        self.assertFalse(self.chess.is_playing())

if __name__ == '__main__':
    unittest.main()