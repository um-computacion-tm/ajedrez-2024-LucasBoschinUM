from game.class_chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        print("Options: ")
        print("1. Move piece")
        print("2. End game by agreement")
        option = int(input("Choose an option: "))
        
        if option == 1:
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
            to_row = int(input("To Row: "))
            to_col = int(input("To Col: "))
            chess.move(from_row, from_col, to_row, to_col)
        elif option == 2:
            chess.end_by_agreement()
        else:
            print("Invalid option")
    except InvalidMove as e:
        print(e)
    except InvalidTurn as e:
        print(e)
    except EmptyPosition as e:
        print(e)
    except Exception as e:
        print("error", e)

if __name__ == '__main__':
    main()

# Para correrlo en mi terminal local:
# export PYTHONPATH=$(pwd)
# python3 game/cli.py
# coverage run -m unittest && coverage xml && coverage report -m