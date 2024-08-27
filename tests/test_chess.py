import unittest
from game.class_chess import Chess
from game.class_board import Board

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.chess._Chess__board__ = Board()  # Inicializar el tablero correctamente

    def test_initial_turn(self):
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

    def test_move_changes_turn(self):
        # Mock the board's get_piece method
        self.chess._Chess__board__.get_piece = lambda x, y: "Pawn"
        self.chess.move(0, 0, 1, 1)
        self.assertEqual(self.chess.turn, "BLACK")

if __name__ == '__main__':
    unittest.main()