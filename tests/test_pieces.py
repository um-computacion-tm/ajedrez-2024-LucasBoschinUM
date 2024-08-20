import unittest
from game.class_pieces import Piece

class TestPiece(unittest.TestCase):
    def test_initialization(self):
        color = "white"
        piece = Piece(color)
        self.assertEqual(piece._Piece__color__, color)

if __name__ == '__main__':
    unittest.main()