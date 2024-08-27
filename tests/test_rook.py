import unittest
from game.class_rook import Rook, Piece

class TestRook(unittest.TestCase):
    
    def setUp(self):
        # Configuración inicial para las pruebas
        self.rook = Rook(__color__='white')  # Proporcionar el argumento '__color__'

    def test_rook_inheritance(self):
        # Verifica que Rook hereda de Piece
        self.assertIsInstance(self.rook, Piece)

    def test_rook_initial_position(self):
        # Verifica la posición inicial del Rook, si hay un método o atributo para esto
        # Ejemplo: self.assertEqual(self.rook.__position__, (0, 0))
        pass

    def test_rook_moves(self):
        # Verifica los movimientos válidos del Rook
        # Ejemplo: self.assertTrue(self.rook.is_valid_move((0, 5)))
        pass

if __name__ == '__main__':
    unittest.main()