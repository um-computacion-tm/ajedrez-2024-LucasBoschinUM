from game.class_pieces import Piece

class Rook(Piece):
    def __init__(self, __color__):
        super().__init__(__color__)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"