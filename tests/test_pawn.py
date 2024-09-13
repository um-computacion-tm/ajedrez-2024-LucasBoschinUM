import unittest
from game.class_pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_white_str(self):
        pawn = Pawn()
        self.assertEqual(pawn.white_str, "♜")

    def test_black_str(self):
        pawn = Pawn()
        self.assertEqual(pawn.black_str, "♖")

if __name__ == '__main__':
    unittest.main()