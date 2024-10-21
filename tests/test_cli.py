import unittest
from game.cli import play, main
from unittest.mock import patch
from game.class_chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1', '2', '2', '3'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 5)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 6)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 6)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    @patch.object(Chess, 'end_by_agreement')
    def test_end_by_agreement(self, mock_end_by_agreement, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 5)
        self.assertEqual(mock_end_by_agreement.call_count, 1)

    @patch('game.cli.play')
    @patch.object(Chess, 'is_playing', side_effect=[True, False])
    def test_main(self, mock_is_playing, mock_play):
        main()
        self.assertEqual(mock_is_playing.call_count, 2)
        self.assertEqual(mock_play.call_count, 1)

if __name__ == '__main__':
    unittest.main()

    # @patch(  # este patch controla lo que hace el input
    #     'builtins.input',
    #     side_effect=['1', '1', '2', '1'], # estos son los valores que simula lo que ingresaria el usuario
    # )
    # @patch('builtins.print') # este patch controla lo que hace el print
    # @patch.object(
    #     Chess,
    #     'move',
    #     side_effect=InvalidMove(),
    # )
    # def test_invalid_move(
    #     self,
    #     mock_chess_move,
    #     mock_print,
    #     mock_input,
    # ): #
    #     chess = Chess()
    #     play(chess)
    #     self.assertEqual(mock_input.call_count, 4)
    #     self.assertEqual(mock_print.call_count, 2)
    #     self.assertEqual(mock_chess_move.call_count, 1)