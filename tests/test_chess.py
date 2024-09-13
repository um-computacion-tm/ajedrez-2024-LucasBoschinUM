import unittest
from game.class_chess import Chess
from game.class_board import Board
from game.class_rook import Rook

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
    # Mock the board's get_piece method to return a white piece
    self.chess._Chess__board__.get_piece = lambda x, y: Rook("WHITE", self.chess._Chess__board__)
    self.chess._Chess__board__.set_piece(7, 0, Rook("WHITE", self.chess._Chess__board__))  # Set a white rook at (7, 0)
    self.chess.move(7, 0, 6, 0)  # Move the white rook from (7, 0) to (6, 0)
    self.assertEqual(self.chess.turn, "BLACK")

if __name__ == '__main__':
    unittest.main()