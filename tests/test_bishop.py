import unittest
from game.class_bishop import Bishop
from game.class_board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test=True)
        self.bishop_white = Bishop("WHITE", self.board)
        self.bishop_black = Bishop("BLACK", self.board)
        self.board.place_piece(self.bishop_white, 4, 4)
        self.board.place_piece(self.bishop_black, 2, 2)

    def test_initialization(self):
        self.assertEqual(str(self.bishop_white), "♗")
        self.assertEqual(str(self.bishop_black), "♝")

    def test_get_possible_positions(self):
        from_row, from_col = 4, 4
        expected_positions = self.bishop_white.possible_diagonal_positions(from_row, from_col)
        self.assertEqual(self.bishop_white.get_possible_positions(from_row, from_col), expected_positions)

    def test_is_move_valid(self):
        # Movimientos válidos para el alfil blanco en (4, 4)
        self.assertTrue(self.bishop_white.is_move_valid(4, 4, 5, 5))
        self.assertTrue(self.bishop_white.is_move_valid(4, 4, 3, 3))
        self.assertTrue(self.bishop_white.is_move_valid(4, 4, 6, 6))
        self.assertTrue(self.bishop_white.is_move_valid(4, 4, 2, 6))

        # Movimientos no válidos para el alfil blanco en (4, 4)
        self.assertFalse(self.bishop_white.is_move_valid(4, 4, 4, 5))
        self.assertFalse(self.bishop_white.is_move_valid(4, 4, 5, 4))
        self.assertFalse(self.bishop_white.is_move_valid(4, 4, 4, 3))
        self.assertFalse(self.bishop_white.is_move_valid(4, 4, 3, 4))

    def test_possible_diagonal_positions_with_opponent_piece(self):
        # Colocar una pieza del color opuesto en una posición diagonal accesible para el alfil blanco
        self.board.place_piece(self.bishop_black, 6, 6)
        # Obtener las posiciones posibles para el alfil blanco desde (4, 4)
        possible_positions = self.bishop_white.possible_diagonal_positions(4, 4)
        # Verificar que el alfil puede moverse a la posición de la pieza del color opuesto y no más allá
        self.assertIn((6, 6), possible_positions)
        self.assertNotIn((7, 7), possible_positions)

    def test_possible_diagonal_positions_with_same_color_piece(self):
        # Colocar una pieza del mismo color en una posición diagonal accesible para el alfil blanco
        self.board.place_piece(self.bishop_white, 6, 6)
        # Obtener las posiciones posibles para el alfil blanco desde (4, 4)
        possible_positions = self.bishop_white.possible_diagonal_positions(4, 4)
        # Verificar que el alfil no puede moverse a través de una pieza del mismo color
        self.assertNotIn((6, 6), possible_positions)
        self.assertNotIn((7, 7), possible_positions)

if __name__ == '__main__':
    unittest.main()