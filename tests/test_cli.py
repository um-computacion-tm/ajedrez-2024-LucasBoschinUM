import unittest
from unittest.mock import patch
from game.class_chess import Chess
from game.cli import play

class TestCli(unittest.TestCase):
    @patch( # este patch controla lo que hace 'builtins.input'
        side_effect=['1', '1', '2', '2'], #es
    )

    @patch('builtins.print') # este patch controla lo que hace 'builtin/bundles/web/images/offline-play/standardboard.1d6f9426.pngs.print'
    def test_happy_path(self, mock_print, mock_input):
        chess = Chess()
        import ipdb; ipdb.set_trace()
        play(chess)