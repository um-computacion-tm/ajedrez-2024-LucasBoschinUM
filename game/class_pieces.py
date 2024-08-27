class Piece:
    def __init__(self, color):
        self.__color__ = color

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def move(self):
        print("Rook moves horizontally or vertically")