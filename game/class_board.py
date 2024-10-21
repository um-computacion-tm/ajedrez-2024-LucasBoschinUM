from game.class_rook import Rook
from game.class_knight import Knight
from game.class_bishop import Bishop
from game.class_queen import Queen
from game.class_king import King
from game.class_pawn import Pawn
from game.exceptions import OutOfBoard

class Board:
    def __init__(self, for_test=False):
        self.__positions__ = []
        for _ in range(8): #Forma del tablero (8 filas, 8 columnas) ; índices de 1-8 & de A-H
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.setup_pieces()

    def setup_pieces(self):
        # Rooks
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][7] = Rook("WHITE", self)
        self.__positions__[7][0] = Rook("WHITE", self)
        # Knights
        self.__positions__[0][1] = Knight('BLACK', self)
        self.__positions__[0][6] = Knight('BLACK', self)
        self.__positions__[7][1] = Knight('WHITE', self)
        self.__positions__[7][6] = Knight('WHITE', self)
        # Bishops
        self.__positions__[0][2] = Bishop('BLACK', self)
        self.__positions__[0][5] = Bishop('BLACK', self)
        self.__positions__[7][2] = Bishop('WHITE', self)
        self.__positions__[7][5] = Bishop('WHITE', self)
        # Queens
        self.__positions__[0][3] = Queen('BLACK', self)
        self.__positions__[7][3] = Queen('WHITE', self)
        # Kings
        self.__positions__[0][4] = King('BLACK', self)
        self.__positions__[7][4] = King('WHITE', self)
        # Pawns
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)
            self.__positions__[6][col] = Pawn("WHITE", self)

    def __str__(self):
        board_str = "  0 1 2 3 4 5 6 7\n"
        for idx, row in enumerate(self.__positions__):
            board_str += f"{idx} "
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += "  "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col): #Método para mover y comer piezas
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def place_piece(self, piece, row, col):
        self.__positions__[row][col] = piece

    def remove_piece(self, row, col):
        self.__positions__[row][col] = None

    def has_no_pieces(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.get_color() == color:
                    return False
        return True