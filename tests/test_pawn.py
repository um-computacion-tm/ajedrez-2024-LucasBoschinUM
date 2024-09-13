import unittest
from game.class_pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_white_str(self):
        pawn = Pawn(color="white", board=None)  # Proporcionar los argumentos necesarios
        self.assertEqual(pawn.white_str, "♜")

    def test_black_str(self):
        pawn = Pawn(color="black", board=None)  # Proporcionar los argumentos necesarios
        self.assertEqual(pawn.black_str, "♖")

if __name__ == '__main__':
    unittest.main()