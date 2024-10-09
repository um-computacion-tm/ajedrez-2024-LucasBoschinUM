import unittest
from game.class_pieces import Piece
from game.class_board import Board

class TestPiece(unittest.TestCase):
    def test_initialization(self):
        color = "WHITE"
        board = Board()
        piece = Piece(color, board)
        self.assertEqual(piece.get_color(), color)

    def test_get_color(self):
        color = "BLACK"
        board = Board()
        piece = Piece(color, board)
        self.assertEqual(piece.get_color(), color)

    def test_get_possible_positions(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        
        # Asumiendo que possible_diagonal_positions y possible_orthogonal_positions
        # están correctamente implementados y devuelven posiciones válidas.
        expected_positions = piece.possible_diagonal_positions(4, 4) + piece.possible_orthogonal_positions(4, 4)
        
        self.assertEqual(piece.get_possible_positions(4, 4), expected_positions)

    def test_possible_positions_vd(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(5, 4), (6, 4), (7, 4)]
        self.assertEqual(piece.possible_positions_vd(4, 4), expected_positions)

    def test_possible_positions_va(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertEqual(piece.possible_positions_va(4, 4), expected_positions)

    def test_str(self):
        board = Board()
        piece_white = Piece("WHITE", board)
        piece_black = Piece("BLACK", board)
        piece_white.white_str = "W"
        piece_black.black_str = "B"
        self.assertEqual(str(piece_white), "W")
        self.assertEqual(str(piece_black), "B")

    def test_valid_positions(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        self.assertTrue(piece.valid_positions(4, 4, 5, 4))
        self.assertFalse(piece.valid_positions(4, 4, 8, 4))

    def test_possible_diagonal_positions(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        self.assertEqual(piece.possible_diagonal_positions(4, 4), [])

    def test_possible_orthogonal_positions(self):
        board = Board(for_test=True)
        piece = Piece("WHITE", board)
        board.set_piece(4, 4, piece)
        expected_positions = [(5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertEqual(piece.possible_orthogonal_positions(4, 4), expected_positions)

    def test_capture_opponent_piece(self):
        board = Board(for_test=True)
        white_piece = Piece("WHITE", board)
        black_piece = Piece("BLACK", board)
        
        # Colocar la pieza blanca en (4, 4)
        board.set_piece(4, 4, white_piece)
        
        # Colocar la pieza negra en (5, 4)
        board.set_piece(5, 4, black_piece)
        
        # Obtener las posiciones posibles para la pieza blanca
        possible_positions = white_piece.possible_positions_vd(4, 4)
        
        # Verificar que la posición de la pieza negra esté en las posiciones posibles
        self.assertIn((5, 4), possible_positions)

if __name__ == "__main__":
    unittest.main()