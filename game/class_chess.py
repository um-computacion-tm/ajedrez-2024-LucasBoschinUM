from game.class_board import Board
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    def is_playing(self):
        # Verificar si el juego debe continuar
        if self.__board__.has_no_pieces("WHITE") or self.__board__.has_no_pieces("BLACK"):
            self.__playing__ = False
        return self.__playing__

    def move(self, from_row, from_col, to_row, to_col):
        # Validar coordenadas
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoard()
        
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()
        
        # Verificar si el juego debe terminar después del movimiento
        if not self.is_playing():
            self.end_game()

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def end_game(self):
        # Finalizar el juego y declarar el ganador o empate
        if self.__board__.has_no_pieces("WHITE"):
            print("BLACK wins!")
        elif self.__board__.has_no_pieces("BLACK"):
            print("WHITE wins!")
        else:
            print("Game ended by mutual agreement.")
        self.__playing__ = False

    def end_by_agreement(self):
        # Permitir que los jugadores decidan terminar la partida de mutuo acuerdo
        self.__playing__ = False
        self.end_game()