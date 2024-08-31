import unittest
from game.class_pieces import Piece
from game.class_board import Board  # Asegúrate de importar la clase Board

class TestPiece(unittest.TestCase):
    def test_initialization(self):
        color = "white"
        board = Board()  # Crear una instancia de Board
        piece = Piece(color, board)  # Pasar color y board al constructor
        self.assertEqual(piece.__color__, color)

if __name__ == '__main__':
    unittest.main()