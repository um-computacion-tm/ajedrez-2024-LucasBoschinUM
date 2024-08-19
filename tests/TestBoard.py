import unittest
from clases.ClassBoard import Board
from clases.ClassPieces import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        # Verificar que las posiciones iniciales de las torres sean correctas
        self.assertIsInstance(self.board._Board__positions__[0][0], Rook)
        self.assertEqual(self.board._Board__positions__[0][0].color, "BLACK")
        self.assertIsInstance(self.board._Board__positions__[0][7], Rook)
        self.assertEqual(self.board._Board__positions__[0][7].color, "BLACK")
        self.assertIsInstance(self.board._Board__positions__[7][0], Rook)
        self.assertEqual(self.board._Board__positions__[7][0].color, "WHITE")
        self.assertIsInstance(self.board._Board__positions__[7][7], Rook)
        self.assertEqual(self.board._Board__positions__[7][7].color, "WHITE")

    def test_get_piece(self):
        # Verificar que el método get_piece funcione correctamente
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")
        self.assertIsNone(self.board.get_piece(4, 4))

if __name__ == '__main__':
    unittest.main()